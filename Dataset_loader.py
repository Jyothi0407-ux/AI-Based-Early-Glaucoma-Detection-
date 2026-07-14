from google.colab import files
import zipfile, os

uploaded = files.upload()  # Upload Dataset.zip

zip_name = list(uploaded.keys())[0]
with zipfile.ZipFile(zip_name, 'r') as z:
    z.extractall('/content/dataset')

print("✅ Extracted!")
print(os.listdir('/content/dataset/Dataset'))
