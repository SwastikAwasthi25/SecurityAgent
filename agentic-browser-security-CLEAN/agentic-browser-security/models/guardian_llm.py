import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


BASE_MODEL = "mistralai/Mistral-7B-v0.1"
import os

LORA_PATH = "C:/Users/Swastik Awasthi/OneDrive/Desktop/hackiitk/guardian_output_new/guardian_lora_v2/checkpoint-2000"



class GuardianLLM:
    def __init__(self):
        print("Loading Mistral 7B v0.1 on RTX 5070 Ti (FP16 mode)...")

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA not available.")

        self.tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

        # 🔥 NO 4-BIT. NO BITSANDBYTES.
        base_model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True
        )

        # Attach LoRA
        self.model = PeftModel.from_pretrained(
            base_model,
            LORA_PATH,
            is_trainable=False
        )

        self.model.eval()

        print("GuardianLLM ready.")

    def generate(self, prompt: str, max_new_tokens: int = 128):
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt"
        ).to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=0.0,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        decoded = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return decoded[len(prompt):].strip()
