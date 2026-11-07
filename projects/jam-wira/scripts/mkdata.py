import json,sys,re
S=sys.argv[1]
tr=json.load(open(S+'/work/cut_transcript.json'))
cuts=json.load(open(S+'/work/cuts.json'))
fix={"DUAL":"DUA","MAMI":"MOMMIES","OKEY":"OKAY"}
words=[]
for seg in tr:
    for w in seg['words']:
        t=w['w'].strip()
        if not t: continue
        if t.startswith('-') and words: words[-1]['t']+=t.upper(); words[-1]['e']=w['e']; continue
        t=re.sub(r'[,.?!]','',t).upper(); t=fix.get(t,t)
        words.append({'t':t,'s':round(w['s'],3),'e':round(w['e'],3),'seg':len([1 for x in tr if x['start']<=w['s']])})
# group: max 3 words, break on segment change or gap>0.25
groups=[];cur=[]
for w in words:
    if cur and (len(cur)>=3 or w['seg']!=cur[-1]['seg'] or w['s']-cur[-1]['e']>0.25 or len(' '.join(x['t'] for x in cur+[w]))>18):
        groups.append(cur);cur=[]
    cur.append(w)
groups.append(cur)
caps=[{'s':g[0]['s'],'e':g[-1]['e'],'w':g} for g in groups]
for i in range(len(caps)-1): caps[i]['e']=min(max(caps[i]['e'],caps[i]['s']+0.3),caps[i+1]['s'])
def find(tok,n=1,after=0):
    c=0
    for w in words:
        if w['s']>=after and w['t'].startswith(tok):
            c+=1
            if c==n: return w
    raise Exception(tok)
T=lambda tok,n=1,after=0: find(tok,n,after)['s']
E=lambda tok,n=1,after=0: find(tok,n,after)['e']
dur=cuts[-1]['out0']/30+(cuts[-1]['f1']-cuts[-1]['f0'])/30
ev=[]  # graphics
sfx=[]
def add_sfx(name,t,vol=0.6): sfx.append({'n':name,'t':round(max(t,0),3),'v':vol})
# HOOK
add_sfx('whoosh',0.0,0.55)
sw=find('SMARTWATCH'); sek=find('SEKOLAH'); haa=find('HAA')
ev.append({'type':'hookTitle','s':0.05,'e':haa['s']+1.2,'x':sw['s'],'ok':sek['s']})
add_sfx('popclick',sw['s'],0.7); add_sfx('ding',sek['s']+0.1,0.5)
ev.append({'type':'punch','s':sw['s'],'e':sw['e']+0.25,'z':1.12})
add_sfx('sparkle',haa['s']-0.05,0.6)
ev.append({'type':'shine','s':haa['s'],'e':haa['s']+0.7})
# TikTok
tk=find('TIKTOK'); ev.append({'type':'pill','s':tk['s'],'e':T('CANTIK')-0.1,'text':'JUMPA DI TIKTOK SHOP','emoji':'🛍️'}); add_sfx('pop',tk['s'],0.6)
# cantik comel
cc=find('CANTIK'); ev.append({'type':'title','s':cc['s'],'e':T('PINK')-0.05,'text':'CANTIK & COMEL','emoji':'💚'}); add_sfx('wand',cc['s'],0.35)
# swatches
pk,pt,gr=find('PINK'),find('PUTIH'),find('GREEN')
grab=find('GRAB')
ev.append({'type':'swatches','s':pk['s'],'e':T('SEE')-0.05,'pink':pk['s'],'white':pt['s'],'green':gr['s'],'pick':grab['s']})
for w in (pk,pt,gr): add_sfx('poplight',w['s'],0.8)
add_sfx('confirm',grab['s']+0.2,0.5)
# see dia cantik -> sparkle
add_sfx('sparkle',T('SEE')+0.1,0.35)
# water resistant
wr=find('WATER'); ev.append({'type':'badge','s':wr['s'],'e':T('SIZE')-0.05,'text':'WATER\nRESISTANT','emoji':'💧','color':'#5EC8FF'}); add_sfx('splash',wr['s']-0.05,0.55); add_sfx('bubble',wr['s']+0.35,0.5)
# size
sz=find('SIZE'); ev.append({'type':'title','s':sz['s'],'e':T('DALAM',1,sz['s'])-0.05,'text':'SAIZ NGAM-NGAM','emoji':'👌'}); add_sfx('popclick',sz['s'],0.6)
# very good
vg=find('VERY'); ev.append({'type':'sticker','s':vg['s'],'e':T('HURUF')-0.1,'text':'VERY GOOD','emoji':'⭐'}); add_sfx('reward',vg['s'],0.5)
ev.append({'type':'punch','s':vg['s'],'e':E('GOOD')+0.3,'z':1.1})
# huruf nombor
hf,nb=find('HURUF'),find('NOMBOR')
ev.append({'type':'chips','s':hf['s'],'e':T('SENANG')+0.2,'a':hf['s'],'b':nb['s']}); add_sfx('poplight',hf['s'],0.8); add_sfx('poplight',nb['s'],0.8)
# senang belajar
sn=find('SENANG'); ev.append({'type':'title','s':sn['s'],'e':T('JARUM')-0.05,'text':'SENANG BELAJAR BACA JAM','emoji':'🕐'}); add_sfx('knob',sn['s'],0.4)
# clock
j1=find('JARUM',1); j2=find('JARUM',2)
ev.append({'type':'clock','s':j1['s']-0.1,'e':T('SILIKON')+0.0,'a':j1['s'],'b':j2['s']}); add_sfx('tick',j1['s'],0.7); add_sfx('tick',j2['s'],0.7)
# silikon
sl=find('SILIKON'); ev.append({'type':'title','s':sl['s'],'e':T('KALAU',1,sl['s'])-0.05,'text':'STRAP SILIKON','emoji':'✅'}); add_sfx('popclick',sl['s'],0.6)
add_sfx('sparkle',T('CANTIK',3)-0.05 if True else 0,0.4)
# bekas tin
bk=find('BEKAS'); ev.append({'type':'badge','s':bk['s'],'e':T('PRESENT')-0.2,'text':'FREE\nBEKAS TIN','emoji':'🎁','color':'#FFD23F'}); add_sfx('whoosh2',bk['s']-0.15,0.45); add_sfx('ding',bk['s']+0.15,0.4)
pr=find('PRESENT'); ev.append({'type':'title','s':pr['s']-0.15,'e':T('MOMMIES')-0.05,'text':'SESUAI JADI HADIAH','emoji':'🎁'}); add_sfx('pop',pr['s']-0.15,0.6)
# CTA
bag=find('BAG'); ev.append({'type':'cta','s':T('TENGOK',1,bag['s']-1.5),'e':dur}); add_sfx('pop',T('TENGOK',1,bag['s']-1.5),0.7)
add_sfx('bubble',bag['s'],0.6)
pk2=find('PINK',2); ev.append({'type':'pinkNote','s':pk2['s'],'e':T('TENGOK',1,pk2['s'])-0.05}); add_sfx('poplight',pk2['s'],0.8)
# zoom pattern per cut segment
segs=[{'s':c['out0']/30,'e':c['out0']/30+(c['f1']-c['f0'])/30} for c in cuts]
data={'fps':30,'dur':round(dur,3),'tail':0.6,'caps':caps,'ev':ev,'sfx':sorted(sfx,key=lambda x:x['t']),'segs':segs}
json.dump(data,open(S+'/rm/src/data.json','w'),ensure_ascii=False,indent=1)
print('dur',dur,'caps',len(caps),'ev',len(ev),'sfx',len(sfx))
for c in caps[:6]: print(round(c['s'],2),' '.join(w['t'] for w in c['w']))
