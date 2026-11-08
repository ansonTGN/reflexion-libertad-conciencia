#!/usr/bin/env python3
"""Generate five static locale pages from the Spanish source and editorial translations."""
from pathlib import Path
from bs4 import BeautifulSoup
from translations import DATA

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT / 'source' / 'index.es.html'
ARTICLE='https://www.larazon.es/cultura/woke-20-virus-muta-sobrevivir_202611086aefb48fea8d8979977d2cd4.html'
CODES=['es','ca','en','pt','fr']
LABELS={'es':'Español','ca':'Català','en':'English','pt':'Português','fr':'Français'}
LOCALES={'es':'es_ES','ca':'ca_ES','en':'en_GB','pt':'pt_PT','fr':'fr_FR'}
HEADINGS=['poder','identidad','ideologias','indignacion','obediencia','pensamiento','etica','libertad']
ES={
 'title':'Cuando las ideologías piensan por nosotros','subtitle':'Una reflexión sobre el poder, la identidad y la libertad de conciencia.',
 'eyebrow':'Pensamiento · Sociedad · Filosofía','date':'8 de noviembre de 2026','kind':'Ensayo filosófico','begin':'Comenzar a leer','contents':'En este ensayo','brand':'Ensayos','share':'Compartir','copy':'Enlace copiado','copy_prompt':'Copia este enlace:','dark':'Tema oscuro','light':'Tema claro','skip':'Saltar al contenido','article_label':'Ensayo completo','caption':'La libertad comienza con una pregunta.','image_alt':'Una persona camina por una biblioteca monumental hacia la luz exterior','top':'Volver al inicio','read_original':'Leer el artículo original ↗','reference':'Artículo de referencia ↗','origin':'Lectura de origen · La Razón','notice':'El artículo pertenece a su medio y puede estar sujeto a sus condiciones de acceso.','footer':'Reflexión y pensamiento crítico'}

def render(code):
    t=ES if code=='es' else DATA[code]
    soup=BeautifulSoup(SOURCE.read_text(encoding='utf-8'),'html.parser')
    soup.html['lang']=code
    head=soup.head
    head.find('title').string=f"{t['title']} · Ángel A. Urbina Sánchez"
    head.find('meta',attrs={'name':'description'})['content']=t['subtitle']+' — Ángel A. Urbina Sánchez.'
    for key,value in [('og:title',t['title']),('og:description',t['subtitle']),('og:locale',LOCALES[code])]:
        head.find('meta',attrs={'property':key})['content']=value
    if code!='es':
        head.find('link',attrs={'rel':'stylesheet'})['href']='/assets/style.css'
        head.find('link',attrs={'rel':'icon'})['href']='/assets/favicon.svg'
        head.find('script',attrs={'src':'assets/site.js'})['src']='/assets/site.js'
        soup.select_one('.hero-visual img')['src']='/assets/biblioteca-libertad.webp'
    head.append(BeautifulSoup('<meta name="robots" content="index,follow">','html.parser'))
    for lg in CODES:
        href='/' if lg=='es' else f'/{lg}/'
        link=soup.new_tag('link',rel='alternate',hreflang=lg,href=href)
        head.append(link)
    head.append(soup.new_tag('link',rel='alternate',hreflang='x-default',href='/'))
    soup.body['data-language']=code
    soup.select_one('.skip-link').string=t['skip']
    brand=soup.select_one('.brand')
    brand.clear()
    brand.append('Ángel A. Urbina Sánchez / '+t['brand'])
    toolbar=soup.select_one('.toolbar')
    select=soup.new_tag('select',id='language-select')
    select['aria-label']={'es':'Idioma del artículo','ca':'Idioma de l’article','en':'Article language','pt':'Idioma do artigo','fr':'Langue de l’article'}[code]
    select['title']=select['aria-label']
    for lg in CODES:
        op=soup.new_tag('option',value=('/' if lg=='es' else f'/{lg}/'))
        op.string=LABELS[lg]
        if lg==code: op['selected']='selected'
        select.append(op)
    wrapper=soup.new_tag('label',attrs={'class':'language-picker'})
    mark=soup.new_tag('span',attrs={'aria-hidden':'true'});mark.string='◎'
    wrapper.append(mark);wrapper.append(select)
    toolbar.insert(0,wrapper)
    share=soup.select_one('#copy-link');share.string='↗ '+t['share']
    switch=soup.select_one('#theme-toggle');switch.string='☾ '+t['dark']
    for key in ['share','copy','copy_prompt','dark','light']:
        soup.body[f'data-{key.replace("_","-")}']=t[key]
    soup.select_one('.eyebrow').string=t['eyebrow']
    soup.select_one('.hero h1').string=t['title']
    soup.select_one('.hero .lead').string=t['subtitle']
    meta=soup.select_one('.hero .meta').find_all('span')
    meta[1].string=t['date'];meta[2].string=t['kind']
    cta=soup.select_one('.hero-cta');cta.clear();cta.append(t['begin']+' ↓')
    soup.select_one('.hero-visual img')['alt']=t['image_alt']
    soup.select_one('.hero-visual figcaption').string=t['caption']
    toc=soup.select_one('.toc')
    toc['aria-label']=t['contents'];toc.strong.string=t['contents']
    for idx,a in enumerate(toc.select('nav a')):
        if code!='es':a.string=t['headings'][HEADINGS[idx]]
    article=soup.select_one('article.article');article['aria-label']=t['article_label']
    if code!='es':
        for sec in article.select('section'):
            sid=sec['id']
            fragment=BeautifulSoup(t['sections'][sid],'html.parser')
            sec.clear()
            if sid!='introduccion':
                h=soup.new_tag('h2',id=f'heading-{sid}')
                h.string=t['headings'][sid]
                sec.append(h)
            for node in list(fragment.contents):sec.append(node)
            if sid=='introduccion':
                box=soup.new_tag('aside',attrs={'class':'source-box','aria-label':t['origin']})
                lab=soup.new_tag('span',attrs={'class':'label'});lab.string=t['origin'];box.append(lab)
                p=soup.new_tag('p');p.string=t['source'];box.append(p)
                a=soup.new_tag('a',href=ARTICLE,target='_blank',rel='noopener noreferrer');a.string=t['read_original'];box.append(a)
                note=soup.new_tag('p');note['class']='small-note';note.string=t['notice'];box.append(note)
                sec.append(box)
        signature=article.select_one('.signature');signature.clear();signature.append(t['signature']+' ')
        a=soup.new_tag('a',href=ARTICLE,target='_blank',rel='noopener noreferrer');a.string=t['read_original'];signature.append(a)
        strong=soup.new_tag('strong');strong.string='Ángel A. Urbina Sánchez';signature.append(strong)
        top=soup.new_tag('a',href='#arriba');top['class']='back-to-top';top.string='↑ '+t['top'];signature.append(top)
    else:
        article.select_one('.back-to-top').string='↑ '+t['top']
    for link in soup.select('a.source-link'):
        link['href']=ARTICLE;link['target']='_blank';link['rel']='noopener noreferrer'
    footer=soup.select_one('.footer');footer.clear()
    footer.append('© 2026 Ángel A. Urbina Sánchez · '+t['footer']+' · ')
    a=soup.new_tag('a',href=ARTICLE,target='_blank',rel='noopener noreferrer');a.string=t['reference'];footer.append(a)
    output=ROOT/'index.html' if code=='es' else ROOT/code/'index.html'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text('<!doctype html>\n'+str(soup.html),encoding='utf-8')
    return output

if __name__=='__main__':
    for code in CODES: print(code, render(code))
