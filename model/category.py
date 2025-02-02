class Category:
    def __init__(self, id, name, image_url, created_at, description):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.created_at = created_at
        self.description = description
      
    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Image URL: {self.image_url}")
        print(f"Name: {self.name}")
        print(f"Created At: {self.created_at}")
        print(f"Description: {self.description}")