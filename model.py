from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSequenceClassification
import time

def getModel():
    model_id = "SamLowe/roberta-base-go_emotions-onnx"
    file_name = "onnx/model_quantized.onnx"

    model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name, provider ="CPUExecutionProvider")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    return model, tokenizer


def getClassifier():
    # model1, tokenizer1 = getModel()

    model_id = "SamLowe/roberta-base-go_emotions-onnx"
    file_name = "onnx/model_quantized.onnx"

    model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name, provider ="CPUExecutionProvider")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    onnx_classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=3,
    function_to_apply="sigmoid",  # optional as is the default for the task
    )
    
    return onnx_classifier

if __name__ == "__main__":

    model_id = "SamLowe/roberta-base-go_emotions-onnx"
    file_name = "onnx/model_quantized.onnx"

    # model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name, provider ="CPUExecutionProvider")
    # tokenizer = AutoTokenizer.from_pretrained(model_id)

    # onnx_classifier = pipeline(
    #     task="text-classification",
    #     model=model,
    #     tokenizer=tokenizer,
    #     top_k=3,
    #     function_to_apply="sigmoid",  # optional as is the default for the task
    # )
    

    classifier = getClassifier()

    start=time.time()
    
    print(classifier("that team is disgrace for the whole city. I feel like we should fire the whole coaching staff"))
    end = time.time()

    length = end - start
    print(f"Code time: {length}s")