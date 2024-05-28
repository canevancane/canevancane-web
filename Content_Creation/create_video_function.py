import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from moviepy.editor import ImageClip, concatenate_videoclips, TextClip, CompositeVideoClip, clips_array, ColorClip

import json

def video_from_JSON(path, title):
    with open(path) as f:
        data = json.load(f)

    # Extract 'Titel' from each entry in the JSON data
    titles = [entry['Titel'] for entry in data]

    # Extract Preis from each entry in the JSON data
    prices = [entry['Preis'] for entry in data]

    # Extract Image URL from each entry in the JSON data
    image_urls = [entry['Image_Link'] for entry in data]

    # Extract Product Link from each entry in the JSON data
    product_links = [entry['Amazon_Link'] for entry in data]

    ######### Function to scale up/down the image #########
    # Define the new size
    new_size = (1920, 1080)

    def resize_image_with_aspect_ratio(img, new_size):
        # Create a new image with black background
        new_img = Image.new("RGB", new_size, "black")

        # Calculate aspect ratio
        ratio = min(new_size[0]/img.size[0], new_size[1]/img.size[1])

        # Calculate the new size of the original image
        img_size = (int(img.size[0]*ratio), int(img.size[1]*ratio))

        # Resize the original image
        img = img.resize(img_size, Image.LANCZOS)

        # Calculate the position to paste the original image
        position = ((new_size[0]-img_size[0])//2, (new_size[1]-img_size[1])//2)

        # Paste the original image into the new image
        new_img.paste(img, position)

        return new_img

    # apply function to every image
    image_location = []

    i = 1

    for url in image_urls:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = resize_image_with_aspect_ratio(img, new_size)
        img.save(f'Content_Creation/Assets/Other Assets/local_image{i}.jpg')
        image_location.append(f'Content_Creation/Assets/Other Assets/local_image{i}.jpg')
        i += 1

    j = 1

    text_overlays = [TextClip(title, fontsize=70, color='black', bg_color='white', size = (1920, 100), font='Arial') for title in titles]

    for i in range(len(text_overlays)):
        text_overlays[i] = text_overlays[i].set_duration(4)
        text_overlays[i] = text_overlays[i].set_pos("bottom")



    # Create a list of ImageClips
    image_clips = [ImageClip(location) for location in image_location]

    # Set the duration of each image clip
    for i in range(len(image_clips)):
        image_clips[i] = image_clips[i].set_duration(4)  # The image will be displayed for 5 seconds

    # concatenate the image clips
    final_image_clip = concatenate_videoclips(image_clips)

    # concatenate the text clips
    final_text_clip = concatenate_videoclips(text_overlays).set_position("bottom")

    main_content_clip = CompositeVideoClip([final_image_clip, final_text_clip])


    # intro with logo and tilte
    logo_clip = ImageClip('Content_Creation/Assets/Logos/Logo.png')
    title_clip = TextClip(f"{title}\n Links in der Beschreibung", fontsize=70, color='white', bg_color='lightcoral', size= new_size, font='Arial')

    logo_clip = logo_clip.set_duration(1)
    title_clip = title_clip.set_duration(3)

    final_clip = concatenate_videoclips([logo_clip, title_clip, main_content_clip])


    # Write the result to a file using the mpeg4 codec
    final_clip.write_videofile("output.mp4", fps=24, codec='mpeg4', bitrate="5000k")

    # Create .txt file with product links

    with open('product_links.txt', 'w') as f:
        i = 0
        for link in product_links:
            f.write(f'{titles[i]}:\n{link}\n\n')
            i += 1


#video_from_JSON("/Users/vincentbecker/Documents/GitHub/canevancane-web/Assets/Desing_Books_Recommendations_05_2024.json", "Design Buch Empfehlungen")
