# import tkinter
from tkinter import *

# import json module
import json

# import create movie function
from create_video_function import video_from_JSON

# create the main window
root = Tk()

# set the window title
root.title("JSON File Creator")

# define function to create JSON file
def create_json():
    name_of_file = entry_json_name.get()

    # Specify the path and name of the file
    file_path = 'Assets/' + name_of_file + '.json'

    # Create an empty dictionary
    data = []

    # Write the empty dictionary to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Empty JSON file created successfully!")

# define function to append to JSON file
def append_json():
    name_of_file = entry_json_name.get()

    # Specify the path and name of the file
    file_path = 'Assets/' + name_of_file + '.json'

    # Read the existing data
    with open(file_path, 'r') as file:
        data = json.load(file)

    titel = entry_title.get()
    subtitel = entry_subtitel.get()
    beschreibung = entry_description.get('1.0', 'end')
    preis = entry_price.get()
    image_link = entry_image_link.get()
    amazon_link = entry_amazon_link.get()

    # Create a new object
    new_data = {
        "Titel": titel,
        "Subtitel": subtitel,
        "Beschreibung": beschreibung,
        "Preis": preis,
        "Image_Link": image_link,
        "Amazon_Link": amazon_link
    }

    # Append the new object to the data
    data.append(new_data)

    # Write the updated data to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Data appended to JSON file successfully!")

    # clear the entry fields
    entry_title.delete(0, END)
    entry_subtitel.delete(0, END)
    entry_description.delete(1.0, END)
    entry_price.delete(0, END)
    entry_image_link.delete(0, END)
    entry_amazon_link.delete(0, END)

# function to create a website


# function to open the overview window
def create_new_window():
    with open("Assets/Overview_articles.json", "r") as file:
        data_existing = json.load(file)

    # extract all elements tilte from data_existing
    title_list = []
    for element in data_existing:
        title_list.append(element["Title"])

    #creating new window
    new_window = Toplevel(root)

    # one label for all elements in title list
    label_title_list = Label(new_window, text="\n".join(title_list))
    label_title_list.pack()

    overview_label = Label(new_window, text="Overview of JSON file", font=("bold",))
    overview_label.pack()

# function to create a website
def create_website():
        web_title = entry_web_title.get()
        web_description = entry_web_description.get('1.0', 'end')
        web_image_link = entry_web_image_link.get()
        web_path = entry_web_path.get()
        web_json_file = "Assets/" + entry_web_json_file.get()

        # HTML Code:
        html_template_code = """
        <!doctype html>
        <html>
        <head>
        <meta charset="UTF-8">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CANÉ VAN CANE</title>
        <link href="main.css" rel="stylesheet" type="text/css">
        </head>

        <body>
        <div class="header-mobile"><a href="index.html">CANÉ</a></div>
        <div class="header"><a href="index.html">CANÉ VAN CANE</a></div>
            <div>
            <h4 class="head-start">{titel}</h4>
            <p class="paragraph"><i>{description}</i></p>
            </div>
            
        <div id="products"></div>
        <script>
        fetch('{path}')
        .then(response => response.json())
        .then(data => {{
            const productsContainer = document.getElementById('products');
            data.forEach(product => {{
            const productDiv = document.createElement('div');
            productDiv.classList.add('product-item'); // Add a class for styling
            
            const title = document.createElement('h4');
            title.textContent = product.Titel;
            title.classList.add('ueberschrift');
            
            const subtitle = document.createElement('h5');
            subtitle.textContent = product.Subtitel;
            subtitle.classList.add('subhead');
                
            const price = document.createElement('p');
            price.textContent = product.Preis;
            price.classList.add('price');
            
            const description = document.createElement('p');
            description.textContent = product.Beschreibung;
            description.classList.add('paragraph');
            
                const imageContainer = document.createElement('div');
            imageContainer.classList.add('image-container'); // Add a class for styling
                
            const image = document.createElement('img');
            image.src = product.Image_Link;
            image.alt = product.Titel;
            image.classList.add('prod_img');
            
                imageContainer.appendChild(image);
                
            const amazonLinkContainer = document.createElement('div'); // Create a container for the kaufen link
            amazonLinkContainer.classList.add('button-container'); // Add a class for styling
            
            const amazonLink = document.createElement('a');
            amazonLink.href = product.Amazon_Link;
            amazonLink.textContent = "Kaufen";
            amazonLink.classList.add('kaufen');
            
            amazonLinkContainer.appendChild(amazonLink); // Append the link to the container
            
            productDiv.appendChild(title);
            productDiv.appendChild(subtitle);
            productDiv.appendChild(price);
            productDiv.appendChild(imageContainer);
            productDiv.appendChild(amazonLinkContainer);
                productDiv.appendChild(description);// Append the link container to the product container
            
            productsContainer.appendChild(productDiv);
            }});
        }});
        </script>
        <footer>
            <p>2024 - CANÉ VAN CANE</p>
        </footer>
        </body>
        </html>
        """
 
        # Use the format method to insert your variables into the HTML template
        html = html_template_code.format(titel=web_title, description=web_description, path=web_json_file)

        path_to_save = web_path + ".html"

        # Write the HTML to a file
        with open(path_to_save, 'w') as f:
            f.write(html)

        # append to JSON overview of Websites
        with open("Assets/Overview_articles.json", "r") as file:
            data_existing = json.load(file)

        # Create a new object
        new_data = {
            "Title": web_title,
            "img": web_image_link,
            "descrp": web_description,
            "path": path_to_save
        }

        # Append the new object to the data
        data_existing.append(new_data)

        # Write the updated data to the file
        with open("Assets/Overview_articles.json", 'w') as file:
            json.dump(data_existing, file, indent=4)

        print("Website appended successfully!")
    



###### Create Labels
## create JSON file
label_create = Label(root, text="Create a new JSON file", font=("bold",))
label_name = Label(root, text="Name:")
entry_json_name = Entry(root, width=50)
entry_json_name.focus_set()
button_creat_json = Button(root, text="Create JSON file", command=create_json)

## append to JSON file
label_append = Label(root, text="Append to JSON file", font=("bold",))
# title
label_title = Label(root, text="Title:")
entry_title = Entry(root, width=50)
# subtitel
label_subtitel = Label(root, text="Subtitel:")
entry_subtitel = Entry(root, width=50)
# description
label_description = Label(root, text="Description:")
entry_description = Text(root, width=65, height=10)
# price
label_price = Label(root, text="Price:")
entry_price = Entry(root, width=50)
# image link
label_image_link = Label(root, text="Image Link:")
entry_image_link = Entry(root, width=50)
# amazon link
label_amazon_link = Label(root, text="Amazon Link:")
entry_amazon_link = Entry(root, width=50)
# append button
button_append = Button(root, text="Append to JSON file", command=append_json)

# open overview button
button_overview = Button(root, text="Overview", command=create_new_window)

############# build webpage
label_web_section = Label(root, text="Create a new website", font=("bold",))

# title of website
label_web_title = Label(root, text="Title Webs.", font=("bold",))
entry_web_title = Entry(root, width=50)

# description of website    
label_web_description = Label(root, text="Desc. Webs.", font=("bold",))
entry_web_description = Text(root, width=65, height=10)

# image link of website
label_web_image_link = Label(root, text="Image Link Webs.", font=("bold",))
entry_web_image_link = Entry(root, width=50)

# path to website
label_web_path = Label(root, text="Name of HTML file", font=("bold",))
entry_web_path = Entry(root, width=50)
entry_web_path.insert(0, entry_web_title.get())

# underlying json file name
label_web_json_file = Label(root, text="Name of JSON file", font=("bold",))
entry_web_json_file = Entry(root, width=50)
entry_web_json_file.insert(0, entry_json_name.get())

# create website button
button_create_website = Button(root, text="Create Website", command=create_website)




###### Build Page
## create JSON file
label_create.grid(row=0, column=1)
label_name.grid(row=1, column=0, sticky=E)
entry_json_name.grid(row=1, column=1)
button_creat_json.grid(row=2, column=1)

## append to JSON file
label_append.grid(row=3, column=1, pady=(10, 0))
label_title.grid(row=4, column=0, sticky=E)
entry_title.grid(row=4, column=1)

label_subtitel.grid(row=5, column=0, sticky=E)
entry_subtitel.grid(row=5, column=1)

label_description.grid(row=6, column=0, sticky=NE)
entry_description.grid(row=6, column=1)

label_price.grid(row=7, column=0, sticky=E)
entry_price.grid(row=7, column=1)

label_image_link.grid(row=8, column=0, sticky=E)
entry_image_link.grid(row=8, column=1)

label_amazon_link.grid(row=9, column=0, sticky=E)
entry_amazon_link.grid(row=9, column=1)

button_append.grid(row=10, column=1)

# open overview button
button_overview.grid(row=11, column=1)

# create webpage
label_web_section.grid(row=12, column=1)

# title of website
label_web_title.grid(row=13, column=0)
entry_web_title.grid(row=13, column=1)

# description of website
label_web_description.grid(row=14, column=0)
entry_web_description.grid(row=14, column=1)

# image link of website
label_web_image_link.grid(row=15, column=0)
entry_web_image_link.grid(row=15, column=1)

# path to website
label_web_path.grid(row=16, column=0)
entry_web_path.grid(row=16, column=1)

# underlying json file name
label_web_json_file.grid(row=17, column=0)
entry_web_json_file.grid(row=17, column=1)

# create website button
button_create_website.grid(row=18, column=1)



########## create second page
# create a new window
button_overview = Button(root, text="Open Overview", command=create_new_window)
button_overview.grid(row=11, column=1)




####### create an event loop
root.mainloop()