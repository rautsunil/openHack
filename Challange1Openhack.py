
# coding: utf-8

# In[1]:


from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry


# In[2]:


# Replace with a valid key
training_key = "1c1dda7a146d4b9c8d6480f0c6e9cde4"
prediction_key = "e9b5ed3daca9415693f31e8ec970248f"


# In[4]:


# Create a new project
trainer = training_api.TrainingApi(training_key)
print ("Creating project...")
project = trainer.create_project("ChalOpenHack1")


# In[5]:


# Make two tags in the new project
hardcell_tag = trainer.create_tag(project.id, "HardCell")
insulated_tag = trainer.create_tag(project.id, "Insulated")


# In[ ]:


import os
hardcell_dir = "/Users/srauz/openhack/gear_images/hardshell_jackets"
for image in os.listdir(os.fsencode("/Users/srauz/openhack/gear_images/hardshell_jackets")):
    with open(hardcell_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
        trainer.create_images_from_data(project.id, img_data.read(), [ hardcell_tag.id ])


insulated_dir = "/Users/srauz/openhack/gear_images/insulated_jackets"
for image in os.listdir(os.fsencode("/Users/srauz/openhack/gear_images/insulated_jackets")):
    with open(insulated_dir + "/" + os.fsdecode(image), mode="rb") as img_data:
        trainer.create_images_from_data(project.id, img_data.read(), [ insulated_tag.id ])
        




# In[ ]:


import time


# In[ ]:


print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status == "Training"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)


# In[ ]:


# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True)
print ("Done!")

