import torch
import torch.nn as nn
import torchvision.models as models
from torchvision import transforms
import cv2
import PIL

class Model(nn.Module):
    def __init__(self, n_input_features):
        super(Model, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)

    def forward(self,x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

FILE = "diffusion.pth"

model = Model(n_input_features=7)

torch.load(FILE)
model.eval()

diffusion_input = PIL.Image.open('tree.jpg')

trans = transforms.Compose([
    transforms.ToTensor()])

diffusion_input_tensor = trans(diffusion_input)
outputs = model(diffusion_input_tensor)
predicted = torch.max(outputs, 1)
cv2.imwrite('generatedimage.jpg', predicted)




# TensorConvert = transforms.ToTensor()
# diffusion_input_tensor = TensorConvert(diffusion_input)
