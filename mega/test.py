import mega

m = Mega.from_credentials("ydnair007@gmail.com","itkimakichut")
                    filename=m.download_from_url(url)
                    print("Downloading Complete Mega :", filename)
