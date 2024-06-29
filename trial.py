import torch

# Path to the .pth file
file_path = "data.pth"

# Load the data from the file
data = torch.load(file_path)

# Print the contents to inspect
print(data)
