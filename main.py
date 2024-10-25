
# TEE PELI TÄHÄN
def Voyager3():  
    import pygame
    import random
    import math
    pygame.init()
    naytto = pygame.display.set_mode((640,480))
    pygame.display.set_caption('To be Voyager 3')
    
    def menu():
        naytto.fill((0,150,254))
        naytto.blit(rob.robo,(0, 355))
        maa.piirra_alusta()
        fontti = pygame.font.SysFont("Arial", 54)
        otsikko = fontti.render(str(f'To be Voyager 3'), True, (0,0,0))
        naytto.blit(otsikko, (170, 50))
        uusi_fontti = pygame.font.SysFont("Arial", 24)
        rivi1 = uusi_fontti.render(str(f'Vie Robotti avaruuteen hyppimällä verson oksia pitkin'), True, (100,0,0))
        rivi2 = uusi_fontti.render(str(f'ja väistele häiritsevää haamua. Pelin kulku nopeutuu ajan kuluessa.'), True, (100,0,0))
        rivi3 = uusi_fontti.render(str(f'Jos putoat ruudun alareunan ulkopuolelle, häviät pelin.'), True, (100,0,0))
        rivi4 = uusi_fontti.render(str(f'Robottia ohjataan nuolinäppäimillä ja ylä-näppäimestä hyppää.'), True, (100,0,0))
        rivi5 = uusi_fontti.render(str(f'Voit hypätä myös ilmasta, mutta sinun on laskeuduttava oksalle,'), True, (100,0,0))
        rivi6 = uusi_fontti.render(str(f'jotta voit hypätä uudestaan.'), True, (100,0,0))
        rivi7 = uusi_fontti.render(str(f'Ylittämällä ruudun sivureunan pääsee toiselle sivustalle.'), True, (100,0,0))
        rivi8 = uusi_fontti.render(str(f'Kerää kolikoita saadaksesi pisteitä. Voitat pelin, kun saat 100 pistettä.'), True, (100,0,0))
        rivi9 = uusi_fontti.render(str(f'Onnea matkaan! Paina "Enter" aloittaaksesi'), True, (100,0,0))
        naytto.blit(rivi1,(20,120))
        naytto.blit(rivi2,(20,150))
        naytto.blit(rivi3,(20,180))
        naytto.blit(rivi4,(20,210))
        naytto.blit(rivi5,(20,240))
        naytto.blit(rivi6,(20,270))
        naytto.blit(rivi7,(20,300))
        naytto.blit(rivi8,(20,330))
        naytto.blit(rivi9, (100,360))
    class Robotti:
        def __init__(self, x:int, y:int):
            self.robo = pygame.image.load("robo.png")
            self.x = x
            self.y = y
            
            
            self.painovoima = 1
            self.hyppykorkeus = 26
            self.nopeus = self.hyppykorkeus
            self.rect = pygame.Rect(self.x,self.y,self.robo.get_width(), self.robo.get_height())
            self.koko_rect = pygame.Rect(self.x,self.y,self.robo.get_width(),self.robo.get_height())
        def paivita_nopeus(self, speed):
            self.hyppykorkeus = speed
        def paivita_x(self, x):
            self.x = x
        def paivita_y(self, y):
            self.y = y
        
        def piirra(self):
            self.koko_rect = pygame.Rect(self.x,self.y,self.robo.get_width(),self.robo.get_height())
            self.rect = pygame.Rect(self.x,self.y+self.robo.get_height()-15,self.robo.get_width(),28 )
            #pygame.draw.rect(naytto,(255,0,0),self.rect)
            naytto.blit(self.robo,(self.x, self.y))
    class Hirvio:
        def __init__(self, x, y):
                self.hirv = pygame.image.load("hirvio.png")
                self.x = x
                self.y = y
                self.y_nopeus = 0
                self.x_nopeus = 0
                self.vasen_rect = pygame.Rect(self.x,self.y, self.hirv.get_width()/2,self.hirv.get_height())
                self.oikea_rect = pygame.Rect(self.x+self.hirv.get_width()/2,self.y, self.hirv.get_width(),self.hirv.get_height())
                
        def paivita_y_nopeus(self, speed):
            self.y_nopeus += speed
        def paivita_x_nopeus(self, speed):
            self.x_nopeus += speed
        def paivita_x(self, x):
            self.x = x
        def paivita_y(self, y):
            self.y = y
        def liike_ylos_alas(self):
            self.y += self.y_nopeus
        def liike_sivuille(self):
            self.x += self.x_nopeus

        def piirra(self):
            self.vasen_rect = pygame.Rect(self.x+5,self.y, self.hirv.get_width()/2,self.hirv.get_height())
            self.oikea_rect = pygame.Rect(self.x+self.hirv.get_width()/2,self.y, self.hirv.get_width()/2-2,self.hirv.get_height())
            #pygame.draw.rect(naytto,(0,255,255),self.vasen_rect)
            #pygame.draw.rect(naytto,(255,0,100),self.oikea_rect)
            naytto.blit(self.hirv,(self.x, self.y))

    class Projektiili:
        def __init__(self, hirvio_x,hirvio_y,kohde_x,kohde_y,nopeus) -> None:
            self.x = hirvio_x
            self.y = hirvio_y
            self.nopeus = nopeus
            x_valim = kohde_x - self.x
            y_valim = kohde_y - self.y
            etaisyys =  math.sqrt(x_valim**2 + y_valim**2)
            self.suunta_x = x_valim/etaisyys
            self.suunta_y = y_valim/etaisyys
            self.rect = pygame.Rect(self.x, self.y, 10, 10)
        def paivita_nopeus(self, nopeus):
            self.nopeus = nopeus
        
        def liike(self):
            self.x += self.suunta_x * self.nopeus
            self.y += self.suunta_y * self.nopeus
            self.rect = pygame.Rect(self.x, self.y, 10, 10)
        def piirra(self):
            pygame.draw.circle(naytto,(255,255,255), (self.x, self.y),10)

    class Kolikko:
        def __init__(self, x, y):
                self.coin = pygame.image.load("kolikko.png")
                self.x = x
                self.y = y
                self.nopeus = 0
                self.rect = pygame.Rect(self.x,self.y, self.coin.get_height(), self.coin.get_width())
        
        
        def paivita_x(self, x):
            self.x = x
        def paivita_y(self, y):
            self.y = y
        
        def piirra(self):
            self.rect = pygame.Rect(self.x,self.y, self.coin.get_height(), self.coin.get_width())
            #pygame.draw.rect(naytto, (0,0,255),self.rect)
            naytto.blit(self.coin,(self.x, self.y))
        def poista_kolikko(self, kolikot:list):
            kolikot.remove(kolikko)

    class Liiku:
            def __init__(self):
                self.painike_paina = pygame.KEYDOWN
                self.painike_eipaina = pygame.KEYUP
                self.painike_oikea = pygame.K_RIGHT
                self.painike_vasen = pygame.K_LEFT
                self.painike_ylos = pygame.K_UP
                
                
                self.oikealle = False
                self.vasemmalle = False
                self.ylos = False
                self.alas = False
            def liike_oikealle(self):
                self.oikealle = True
            def liike_vasemmalle(self):
                self.vasemmalle = True        
            def liike_ylos(self):
                self.ylos = True
            def liike_alas(self):
                self.alas = True    

    class Liikerajat:
        def __init__(self):
            self.ylareuna = 0
            self.alareuna = 480
            self.vasensivu = 0
            self.oikeasivu = 640

    class Pisteet:
            def __init__(self):
                self.koko_pist = 0
                
            def lisaa_piste(self):
                self.koko_pist += 1


    class Varsi:
        def __init__(self) -> None:
            
            self.x = 320
            self.y = 480
            self.aloitus_y = 460
        def kasvu(self): #Kasvattaa verson vartta, kunnes y-akseli on 40, tämän jälkeen kasvu hidastuu merkittävästi. Kun pelin pääsee läpi, varren kasvu lähtee vastakkaiseen suuntaan
            if self.y < 80:
                self.y -= 0.0001
            if self.y > 40:
                self.y -= 0.9
            if pist.koko_pist >= 100:
                self.y += 4
                rob.y -= 4
        
        def y_nyt(self):
            return self.y
        
        def piirra(self):
            self.varsi = pygame.draw.line(naytto,(0,255,0),(320,self.aloitus_y),(320,self.y),20)

    class Oksa: #Oksien pituus, kasvusuunta ja kasvunopeus on satunnaistettu 
        def __init__(self,y:int, suunta) -> None:
            self.vasen_x = varsi.x - 9
            self.oikea_x = varsi.x + 11
            
            self.y = y
            self.suunta = suunta
            self.vasen_x_max = random.randint(80,250)
            self.oikea_x_max = random.randint(440,490)
            self.oikea_pit = self.oikea_x_max-self.oikea_x
            self.vasen_pit = self.vasen_x-self.vasen_x_max
            self.vasen_rect = pygame.Rect(self.vasen_x_max,self.y,self.vasen_pit,5)
            self.oikea_rect = pygame.Rect(self.oikea_x,self.y,self.oikea_pit,5)
            
        
        def o_kasvu_vas(self):
            self.vasen_x -= random.randint(4,7) 
        def o_kasvu_oik(self):
            self.oikea_x += random.randint(4,7) 
        
        def piirra_oik(self):
            self.oksa = pygame.draw.line(naytto,(0,255,0),(320,self.y),(self.oikea_x,self.y),5)
            
        def oikea_pysaytys(self):
            
            self.oksa = pygame.draw.rect(naytto,(0,255,0),self.oikea_rect)
            
        def piirra_vas(self):
            self.oksa = pygame.draw.line(naytto,(0,255,0),(320,self.y),(self.vasen_x,self.y),5)
            
        
        def vasen_pysaytys(self):
            self.oksa =  pygame.draw.rect(naytto,(0,255,0),self.vasen_rect)
        
        def poista_oksa(self,oksat:list):
            oksat.remove(oksa)    
        

            
    class Maa_alusta():
        def __init__(self) -> None:
            self.alusta = pygame.Rect(0-rob.robo.get_width(),440,640+(rob.robo.get_width()*2),40)
        def piirra_alusta(self):
            pygame.draw.rect(naytto,(100,40,0),self.alusta)


    
    def suunta_valittu(): #Oksien suunnan satunnaistaja
        suunnat = ('v','o')
        valinta = random.choice(suunnat)    
        
        return valinta

    def uusi_oksa():
        
        y = varsi.y_nyt() + 20 #Uusi oksa lähtee kasvamaan hieman alempana varren y-akselista
        suunta = suunta_valittu()
        return Oksa(y, suunta)

    def uusi_kolikko():
        y = -50
        x = random.randint(100,500)
        return Kolikko(x,y)

    def uusi_projektiili(): #Hirvion ammukset. Niiden nopeus riippuu pelaajan sen hetkisestä pistemäärästä
        if pist.koko_pist <= 50:
            projekt.nopeus = 4
        elif pist.koko_pist > 50:
            projekt.nopeus = 7
        
        return Projektiili(hirvio.x,hirvio.y,rob.x,rob.y,projekt.nopeus)


    class Hyppy:
        def __init__(self) -> None:
            self.voiko_hypata = 1

        def hyppy_kaytetty(self):
            self.voiko_hypata = 0
        def uusi_hyppy(self):
            self.voiko_hypata = 1

        def hyppy(self):
            
            rob.y -= rob.nopeus
            rob.nopeus -= rob.painovoima
            
                
            if rob.nopeus < -rob.hyppykorkeus:
                liike.ylos = False
                rob.nopeus = rob.hyppykorkeus
                self.hyppy_kaytetty()


    def kamera_ylos_sim(robotti): #Simuloi kameran liikettä ylöspäin, eli lisää objektien y-akselia 
        
        
        if varsi.y <= 50:
            robotti.y += 2
            maa.alusta[1] += 2
            kolikko.y += 2 #Kolikoissa on bugi jos niitä on ruudulla useampi samanaikaisesti, osa lakkaa liikkumasta alaspäin. En keksinyt mikä on syynä tai kuinka ratkaista.
            
            if varsi.aloitus_y <= 480:
                varsi.aloitus_y += 2

    def peli_lapi():
        rob.paivita_y(-1000)
        
        robo_kuva = pygame.transform.rotate(pygame.image.load("robo.png"), 30)
        
        naytto.fill((0,0,0))
    
        pygame.draw.circle(naytto, (0,130,255),(320,1340),900)
        pygame.draw.circle(naytto, (255,255,255),(620,400),1)
        pygame.draw.circle(naytto, (255,255,255),(520,220),1)    
        pygame.draw.circle(naytto, (255,255,255),(220,100),1)    
        pygame.draw.circle(naytto, (255,255,255),(100,350),1)
        pygame.draw.circle(naytto, (255,255,255),(420,40),1)
        pygame.draw.circle(naytto, (255,255,255),(210,90),1)
        pygame.draw.circle(naytto, (255,255,255),(50,290),1)
        pygame.draw.circle(naytto, (255,255,255),(160,130),1)
        
        
        naytto.blit(robo_kuva,(180,300))
        lapi = fontti.render(str(f'Voyager 3 on laukaistu onnistuneesti. Voitit pelin!'), True, (0,0,255))        
        naytto.blit(lapi, (120,240))

    def game_over():
        
        robo_kuva = pygame.transform.rotate(pygame.image.load("robo.png"), 180)
        
        maa = pygame.Rect(0-rob.robo.get_width(),440,640+(rob.robo.get_width()*2),40)
        naytto.fill((0,150,255))
        naytto.blit(hirvio.hirv, (440,120))
        pygame.draw.circle(naytto, (255,255,255),(465,145),8,0,False,False,True,True)
        havis = fontti.render(str(f'Hävisit pelin, harmittaahan se. Sait {pist.koko_pist} pistettä'), True, (255,0,255))        
        uudestaan = fontti.render(str(f'Paina "Enter" aloittaaksesi alusta'), True, (255,0,255))
        naytto.blit(havis, (120,240))
        naytto.blit(uudestaan, (120,300))
        naytto.blit(robo_kuva,(180,400))
        pygame.draw.rect(naytto, (100,40,0), maa)
        
    class Taustavari:
        def __init__(self) -> None:
            self.sininen = 254
            self.vihrea = 150
        def vah_sini(self):
            self.sininen -= 2.5
        def vah_vihr(self):
            self.vihrea -= 2.5
    
    kello =  pygame.time.Clock()
    rob = Robotti(0,0)
    hyp = Hyppy()
    hirvio = Hirvio(-20,-250)
    liike = Liiku()
    rajat = Liikerajat()
    varsi = Varsi()

    oksa = Oksa(450, '')
    maa = Maa_alusta()
    rob.paivita_y(480-rob.robo.get_height())
    pist = Pisteet()
    fontti = pygame.font.SysFont("Arial", 24)
    projekt = Projektiili(hirvio.x,hirvio.y,rob.x,rob.y,4)
    varit = Taustavari()
    peli_havio = False
    oksat = []
    kolikot = []
    projektiilit = []
    oksa_ajastin = 0
    kolikko_ajastin = 0
    projekt_ajastin = 0
    pimeneva_taivas_ajastin = 0
    peli_paalla = False

    def painovoima(robotti): #Jos robotti on oksalla sen oma y-akseli ei lisäänny.
            


            if robotti.rect.colliderect(oksa.vasen_rect): 
                robotti.y += 0
                 
            elif robotti.rect.colliderect(oksa.oikea_rect):
                robotti.y += 0
                
            else:
                robotti.y += 2
                

    def oksa_vasen_tormaus(robotti, oksat):
        for i in oksat:
            if robotti.rect.colliderect(oksa.vasen_rect):
                        liike.ylos = False
                        robotti.nopeus = robotti.hyppykorkeus
                        robotti.y = oksa.y - robotti.robo.get_height()           
                        hyp.uusi_hyppy()
                        break    
                        
                        
        
    def oksa_oikea_tormaus(robotti, oksat):
        for i in oksat:
            if robotti.rect.colliderect(oksa.oikea_rect):
                        liike.ylos = False
                        robotti.nopeus = robotti.hyppykorkeus
                        robotti.y = oksa.y - robotti.robo.get_height() 
                        hyp.uusi_hyppy()
                        break

    def hirvio_tormays(robotti,hirvio):
        osuma = 100
        
        if robotti.koko_rect.colliderect(hirvio.vasen_rect):
            liike.oikealle = False
            liike.ylos = False
            while osuma > 0:
                robotti.x -= 0.1
                osuma -= 1
        if robotti.koko_rect.colliderect(hirvio.oikea_rect):
            liike.vasemmalle = False
            liike.ylos = False
            while osuma > 0:
                robotti.x += 0.1
                osuma -= 1                 
    

    
    while True:
            
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    exit()
            
                if tapahtuma.type == liike.painike_paina:
                    if peli_paalla == False:
                        if tapahtuma.type == pygame.KEYDOWN:
                            if tapahtuma.key == pygame.K_RETURN:
                                peli_paalla = True
                    
                   


                    if peli_havio == True:
                        if tapahtuma.type == pygame.KEYDOWN:
                            if tapahtuma.key == pygame.K_RETURN:
                                Voyager3()
                    
                    if tapahtuma.key == liike.painike_oikea:
                        
                        liike.liike_oikealle()
                    if tapahtuma.key == liike.painike_vasen:
                        liike.liike_vasemmalle()
                    
                    if tapahtuma.key == liike.painike_ylos:
                        liike.liike_ylos()

                if tapahtuma.type == liike.painike_eipaina:
                    if tapahtuma.key == liike.painike_oikea:
                        liike.oikealle = False
                
                    if tapahtuma.key == liike.painike_vasen:
                        liike.vasemmalle = False
            
                    
            if peli_paalla == False:
                menu()
            
            if peli_paalla == True:
            
                if liike.oikealle:
                    if rajat.oikeasivu <= rob.x:
                        rob.x = 0 - rob.robo.get_width()
                    else: 
                        rob.x += 10
                
                if liike.vasemmalle:
                    if rajat.vasensivu >= rob.x+rob.robo.get_width():
                        rob.x = 640 + rob.robo.get_width()
                    else:
                        rob.x -= 10    
                if liike.ylos and hyp.voiko_hypata == 1:
                    hyp.hyppy()    
                    
                nyt = pygame.time.get_ticks() 
                if nyt - oksa_ajastin >= 1500: 
                    oksa_ajastin = nyt
                    oksat.append(uusi_oksa())
                
                nyt2 = pygame.time.get_ticks()
                if pist.koko_pist <= 50:
                    kolik_sec_kello = 5000
                if pist.koko_pist > 50:
                    kolik_sec_kello = 3000
                if nyt2 - kolikko_ajastin >= kolik_sec_kello:
                    kolikko_ajastin = nyt2
                    kolikot.append(uusi_kolikko())
                    
                nyt3 = pygame.time.get_ticks()
                if pist.koko_pist <= 75:
                    pr_sec_kello = 9000
                if pist.koko_pist > 75:
                    pr_sec_kello = 6000
                elif pist.koko_pist > 90:
                    pr_sec_kello = 3000
                if nyt3 - projekt_ajastin > pr_sec_kello:
                    projekt_ajastin = nyt3
                    projektiilit.append(uusi_projektiili())
                    
                
                nyt4 = pygame.time.get_ticks() #tausta tummenee mitä pidemmälle peli etenee
                if nyt4 - pimeneva_taivas_ajastin > 8000:
                    pimeneva_taivas_ajastin = nyt4
                    if varit.vihrea >= 0:
                        varit.vah_vihr()
                    elif varit.vihrea <= 0 and varit.sininen >= 0:
                        varit.vah_sini()


                kamera_ylos_sim(rob)
                
                naytto.fill((0,varit.vihrea,varit.sininen))
                teksti = fontti.render(str(f'Pisteet: {pist.koko_pist}'), True, (255,0,0))
                naytto.blit(teksti, (500,10))
                
                maa.piirra_alusta()
                varsi.kasvu()
                varsi.piirra()
                rob.piirra()
                if rob.y < -250:
                    peli_lapi()
                    hirvio.paivita_x(1000)
                    hirvio.paivita_y(1000)

                if hirvio.y > 600: #tässä määritettään, kuinka nopeasti hirviö liikkuu. Sen nopeus on määräytyy pelaajan pistemäärästä
                    if pist.koko_pist <= 25:
                        hirvio.y_nopeus = -2
                        hirvio.paivita_y_nopeus(hirvio.y_nopeus)
                    elif pist.koko_pist > 25:
                        hirvio.y_nopeus = -3
                        hirvio.paivita_y_nopeus(hirvio.y_nopeus)
                if hirvio.y < -200:
                    if pist.koko_pist <= 25:
                        hirvio.y_nopeus = 2
                        hirvio.paivita_y_nopeus(hirvio.y_nopeus)
                    elif pist.koko_pist > 25:
                        hirvio.y_nopeus = 3
                        hirvio.paivita_y_nopeus(hirvio.y_nopeus)
                if hirvio.x < 0:
                    if pist.koko_pist <= 25:
                        hirvio.x_nopeus = 2
                        hirvio.paivita_x_nopeus(hirvio.x_nopeus)
                    elif pist.koko_pist > 25:
                        hirvio.x_nopeus = 3
                        hirvio.paivita_x_nopeus(hirvio.x_nopeus)
                if hirvio.x > 640:
                    if pist.koko_pist <= 25:
                        hirvio.x_nopeus= -2
                        hirvio.paivita_x_nopeus(hirvio.x_nopeus)
                    elif pist.koko_pist > 25:
                        hirvio.x_nopeus = -3
                        hirvio.paivita_x_nopeus(hirvio.x_nopeus)
                hirvio.liike_ylos_alas()
                hirvio.liike_sivuille()
                hirvio.piirra()
                if peli_havio == True:
                    hirvio.paivita_x(1000)

                

                if pist.koko_pist < 100:
                    hirvio_tormays(rob,hirvio)    
                
                if rob.y > 580:
                    rob.paivita_y(1000)
                    peli_havio = True
                    game_over()

                for pro in projektiilit:
                    pro.liike()
                    pro.piirra()
                    if rob.koko_rect.colliderect(pro.rect) and pist.koko_pist < 100: #Jos hirviön ammus osuu pelaajaan se pysäyttää liikkeen ja vähentää pisteen
                        liike.ylos = False
                        liike.oikealle = False
                        liike.vasemmalle = False
                        pist.koko_pist -= 1
                        projektiilit.remove(pro)
                    elif pro.x < -80 or pro.x > 750 or pro.y < -90 or pro.y > 640: #Jos ammus menee yli rajojen tai peli loppuu, se poistetaan
                        projektiilit.remove(pro)
                    elif pist.koko_pist >= 100:
                        projektiilit.remove(pro)
                    elif peli_havio == True:
                        projektiilit.remove(pro)
                        break
                
                if rob.rect.colliderect(maa.alusta):
                    rob.paivita_y(maa.alusta[1] - rob.robo.get_height())
                    hyp.uusi_hyppy()
                
                for kolikko in kolikot:
                    kolikko.piirra()
                    if kolikko.rect.colliderect(rob.koko_rect):
                        kolikko.poista_kolikko(kolikot)
                        pist.lisaa_piste()
                    elif kolikko.y > 500:
                        kolikko.poista_kolikko(kolikot)
                    elif peli_havio == True:
                        kolikko.poista_kolikko(kolikot)
                        break
                
                for oksa in oksat:
                    if peli_havio == True:
                        break

                    if oksa.suunta == 'v': #Kun oksan suunta on valikoitunut, sitä piiretään niin kauan kunnes se kohtaa satunnaisesti saamansa pituuden.  
                        oksa.o_kasvu_vas()  #Kun oksa saavuttaa saamansa pituuden, se piiretään alustana, jolla pelaaja voi seistä.
                        if varsi.y < 320:
                            if oksa.vasen_x < oksa.vasen_x_max and pist.koko_pist <= 100: 
                                oksa.vasen_pysaytys()    
                            
                            if oksa.vasen_x > oksa.vasen_x_max and pist.koko_pist <= 100:
                                oksa.piirra_vas()    
                            if pist.koko_pist < 100:
                                oksa_vasen_tormaus(rob, oksat)
                    
                    if oksa.suunta == 'o':
                        oksa.o_kasvu_oik()
                        if varsi.y < 320:
                            if oksa.oikea_x > oksa.oikea_x_max and pist.koko_pist <= 100:
                                oksa.oikea_pysaytys()
                            
                            if oksa .oikea_x < oksa.oikea_x_max and pist.koko_pist <= 100:
                                oksa.piirra_oik()
                            
                            if pist.koko_pist < 100:
                                oksa_oikea_tormaus(rob, oksat)
                            
                    painovoima(rob)
                    
                    if oksa.y > 500: #Jos oksa menee ruudun alarajan alle, se poistetaan
                        oksa.poista_oksa(oksat)
                    

                    if varsi.y <= 50:
                        
                        oksa.y += 2
                        
                        oksa.vasen_rect[1] += 2  
                        oksa.oikea_rect[1] += 2

                    elif varsi.y >= 50 and pist.koko_pist >= 100:
                        
                        if liike.ylos == True:
                            liike.ylos = False
                            
                        oksa.y += 4
                        oksa.vasen_rect[1] += 4
                        oksa.oikea_rect[1] += 4
                    
                    
            pygame.display.flip()

            kello.tick(60)
Voyager3()