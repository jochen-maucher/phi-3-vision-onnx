import onnxruntime_genai as og

model = og.Model("cuda-int4-rtn-block-32")
processor = model.create_multimodal_processor()
tokenizer_stream = processor.create_stream()

prompt = '''<|user|>
<|image_1|>
Convert the table to markdown<|end|>
<|assistant|>
'''

images = og.Images.open(*["screenshot.png"])

inputs = processor(prompt, images=images)

params = og.GeneratorParams(model)
params.set_inputs(inputs)
params.set_search_options(max_length=7680)

generator = og.Generator(model, params)

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end="", flush=True)

del generator