# import hub

# dataset_path = 'hub://activeloop/mnist-train'
# ds = hub.load(dataset_path)


# # Indexing
# W = ds.images[0].numpy() # Fetch an image and return a numpy array
# X = ds.labels[0].numpy(aslist=True) # Fetch a label and store it as a 
#                                      # list of numpy arrays

# # Slicing
# Y = ds.images[0:100].numpy() # Fetch 100 images and return a numpy array
#                              # The method above produces an exception if 
#                              # the images are not all the same size

# Z = ds.labels[0:100].numpy(aslist=True)

import hub
print(hub.list('activeloop'))