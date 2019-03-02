# Greining Reiknirita

## Kvik Bestun (Dynamic Programming)

1. Skilgreinum lausnina endurkvæmt
    - Í mæltu máli, og 
    - Með formúlum/teikningum.
2. Byggja lausnina á endurkvæmni upp á við út frá leystum tilvikum (Byrja á grunntilvikum).
3. Skilgreinum gagnagrind til að geyma lausnir á fyrri tilvikum
    - Oft einvíð eða tvívíð fylki.
4. Finna góða útreikningsröð.
    - Einvítt yfirleitt uppávið.
    - Tvívítt gjarnan bara öðru megin við hornalínu.
5. Skrifa út forritið.
    - Notum endurkvæmu skilgreininguna til að fylla upp í hólf.


## Mismunajöfnur & Tímaflækja

Mismunajöfnurnar eru á forminu $$ T(n) = rT(n/c)+f(n) $$ þar sem $$r$$ er fjöldi endurkvæmra kalla í hverju kalli og $$c$$ er fjöldi skiptinga. Við gerum ráð fyrir að $$T(1) = 1$$, þ.e. fastur tími. Lausnin á slíkri mismunajöfnu er $$\sum_{i=1}^Lr^if(n/c^i)$$

Við höfum þumalputtareglur eftir því hvernig liðirnir í summunni haga sér:

- Ef summan er lækkandi kvótaröð (einnig $r < c$), rótin ráðandi, þá er tímaflækjan $$T(n) = \Theta (f(n))$$
- Ef liðirnir í summuni hafa sama gildið (einnig $r=c$) þá er tímaflækjan $$T(n) = \Theta (log(n)f(n))$$ 
- Ef summan er hækkandi kvótaröð (einnig $r > c$), laufin ráðandi, þá er $$T(n) = \Theta (n^{Log_c (r)})$$
    
\end{enumerate}
