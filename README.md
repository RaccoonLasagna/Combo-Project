This is the AI side of the Combo Project.

DiffusionModelTrees.ipybn is the code used to train a diffusion model with the purpose of generating a new images of landscapes when input with an image of a tree. The images used to train the model is obtained from scraping the website "Unsplash". Images used to train are not attached, as there are 15.8 GB of 1,840 images that GitHub won't let me upload.

diffusion.pth is the file name of the trained diffusion model.

diffusion.py is not complete. It is the file that will load the trained diffusion model, diffusion.pth, and recieve images to generate new images. All of this will be done with streamlit to be on a browser.

scraping.py is the code used to scrape tree images from Unsplash.com used to train the diffusion model.

styletransfer.py is the code for using the pretrained Neural style transfer model from Tensorflow to blend two images to create an image which looks similar to one of the original images, "painted" in the art style of the other image.

When the project is completed, DiffusionModelTrees.ipybn will be able to generate landscape images when input with an image. Then, the code from DiffusionModelTrees.ipybn will be combined with styletransfer.py in order to create a prototype webapp that takes two images as an input; one will be for image generation, while the other is used for image stylization. The code will then be sent over to by friend to be deployed on the website.
