import os
import shutil

root = '/data/mtu/datasets/cityscapes'

# Create directories for storing the image, label pairs
if os.path.exists('A'):
    shutil.rmtree('A')
if os.path.exists('B'):
    shutil.rmtree('B')
os.mkdir('A')
os.mkdir('A/test')
os.mkdir('B')
os.mkdir('B/test')

# Copy files into directories created
label_dir = "/data/mtu/HRNet-Semantic-Segmentation/output/cityscapes/seg_hrnet_w48_train_512x1024_sgd_lr1e-2_wd5e-4_bs_12_epoch484/test_results"
if os.path.exists(label_dir + "/.ipynb_checkpoints"):
    shutil.rmtree(label_dir + "/.ipynb_checkpoints")
filenames = os.listdir(label_dir)
for i, f in enumerate(filenames):
    city, num1, num2, _ = f.split('_')

    # Copy image and label files
    label = shutil.copy(label_dir + "/" + f, 'A')
    image = shutil.copy("{}/leftImg8bit/test/{}/{}_{}_{}_leftImg8bit.png".format(root, city, city, num1, num2), 'B')

    # Rename files to have the same name
    os.rename(image, 'A/test/{:06d}.png'.format(i))
    os.rename(label, 'B/test/{:06d}.png'.format(i))
