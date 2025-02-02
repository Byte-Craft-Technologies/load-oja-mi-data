import os

store_path = "./images"
server_address = "http://localhost:8080"

def save_image(image_file,image_name,directory_name):
    directory_path = f"{store_path}/{directory_name}"
    os.makedirs(directory_path,exist_ok=True)
    image_path= f"{directory_path}/{image_name}.png"
    image_file.save(image_path)
    return f"{server_address}/api/{directory_name}/{image_name}"