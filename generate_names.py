import os
import json

PHOTO_DIR = "raw_photos"
OUTPUT_DIR = "photos"

os.makedirs(OUTPUT_DIR, exist_ok=True)

result=[]

files=sorted(os.listdir(PHOTO_DIR))

for idx,file in enumerate(files,start=1):

    ext=os.path.splitext(file)[1]

    photographer=os.path.splitext(file)[0]

    new_name=f"{idx:03d}{ext}"

    os.rename(
        os.path.join(PHOTO_DIR,file),
        os.path.join(OUTPUT_DIR,new_name)
    )

    result.append({
        "id":f"{idx:03d}",
        "photographer":photographer
    })

with open(
    "photographers.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=4
    )

print("完成")