from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSequenceClassification
import time




model_id = "SamLowe/roberta-base-go_emotions-onnx"
file_name = "onnx/model_quantized.onnx"

model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name, provider ="CPUExecutionProvider")
tokenizer = AutoTokenizer.from_pretrained(model_id)

start=time.time()

onnx_classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=3,
    function_to_apply="sigmoid",  # optional as is the default for the task
)



print(onnx_classifier("that team is disgrace for the whole city. I feel like we should fire the whole coaching staff"))
end = time.time()

length = end - start
print(f"Code time: {length}s")