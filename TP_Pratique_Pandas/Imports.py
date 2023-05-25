import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
import pynsee.download

df = pd.read_csv("https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert",
                 sep=",")

df_city = pynsee.download.download_file("FILOSOFI_COM_2016")