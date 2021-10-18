# FlaskImgPngToTxt
Converting PNG to TXT using Tesseract Image to string.

#Building an Image for Docker. 

    docker build -t tesserpact .
    
#Running Image as container.

    docker run -d -p 8080:8080 tesserpact
  
#I have included a test PNG but feel free to try your own!

You can download your file using the client.py file
ClientV2.py is a work in process as it is going to be able to take advantage of a swarm.
