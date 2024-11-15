from bs4 import BeautifulSoup


def pagina():
    return """
     <html>
        <head>
             <title> Prueba</title>


        <body>
             <div> id="main"
                 <h1> Titulo pagina</h1>
                 <p> primer parrafo </p>
                 <p> segundo parrafo </p>
                 <a> href="www.nintendo.com"</a>
                 <div class = "innerClass">
                      <div id "test" class = "link" name="nombre">
                         <a href="www.gogle.com"> Google</a>
                         <a href="www.facebook.com"> Facebook</a>

                      </div>
                      <div class = "Right">
                           <div class = "link">
                             <a href="www.gogle.com"> Google2</a>
                             <a href="www.facebook.com"> Facebook2</a>
                           </div>

                      </div>      

                 </div>


             </div> 


        </body>

     </head>

     </html>
    """


def repaso():
    htmlpagina = pagina()
    soup = BeautifulSoup(htmlpagina, "html5lib")
    # print(soup.p) nomas regresara el primero que encuentre
    # print(soup.div.div.div.a)
    # div = soup.div.div.div.next_sibling.next_sibling #
    # print(type(div))
    # print(div["name"]) #Es un diccionario los div

    ligas = soup.find_all("div", attrs={"class": "link"})  # Agarra todos los enlaces

    for i in ligas:
        liga2 = i.find_all("a")
        for j in liga2:
            print(j.text)