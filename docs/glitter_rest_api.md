---
title: Rest API
nav_order: 8
---

# Rest API



## `process-conllu` POST

Example payload
```
# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe
# udpipe_model = czech-pdt-ud-2.15-241121
# udpipe_model_licence = CC BY-NC-SA
# newdoc
# newpar
# sent_id = 1
# text = STEM: ANO posiluje, Spolu klesá
1	STEM	STEM	NOUN	BNXXX-----A----	Abbr=Yes	0	root	_	SpaceAfter=No|TokenRange=0:4
2	:	:	PUNCT	Z:-------------	_	4	punct	_	TokenRange=4:5
3	ANO	ANO	PROPN	BNXXX-----A----	Abbr=Yes	4	nsubj	_	TokenRange=6:9
4	posiluje	posilovat	VERB	VB-S---3P-AAI--	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin|Voice=Act	1	appos	_	SpaceAfter=No|TokenRange=10:18
5	,	,	PUNCT	Z:-------------	_	7	punct	_	TokenRange=18:19
6	Spolu	spolu	ADV	Db-------------	_	7	advmod	_	TokenRange=20:25
7	klesá	klesat	VERB	VB-S---3P-AAI--	Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin|Voice=Act	4	conj	_	SpacesAfter=\n\n|TokenRange=26:31

# newpar
# sent_id = 2
# text = Hnutí ANO ve volebním modelu agentury STEM pro CNN Prima News od minulého týdne posílilo zhruba o procentní bod na 31,2 procenta.
1	Hnutí	hnutí	NOUN	NNNS1-----A----	Case=Nom|Gender=Neut|Number=Sing|VerbForm=Vnoun	15	nsubj	_	TokenRange=33:38
2	ANO	ANO	PROPN	BNXXX-----A----	Abbr=Yes	1	nmod	_	TokenRange=39:42
3	ve	v	ADP	RV--6----------	AdpType=Voc|Case=Loc	5	case	_	TokenRange=43:45
4	volebním	volební	ADJ	AAIS6----1A----	Animacy=Inan|Case=Loc|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos	5	amod	_	TokenRange=46:54
5	modelu	model	NOUN	NNIS6-----A----	Animacy=Inan|Case=Loc|Gender=Masc|Number=Sing	1	nmod	_	TokenRange=55:61
6	agentury	agentura	NOUN	NNFS2-----A----	Case=Gen|Gender=Fem|Number=Sing	5	nmod	_	TokenRange=62:70
7	STEM	STEM	NOUN	BNXXX-----A----	Abbr=Yes	6	nmod	_	TokenRange=71:75
8	pro	pro	ADP	RR--4----------	AdpType=Prep|Case=Acc	9	case	_	TokenRange=76:79
9	CNN	CNN	PROPN	BNXXX-----A----	Abbr=Yes|NameType=Oth	6	nmod	_	TokenRange=80:83
10	Prima	Prima	X	F%-------------	Foreign=Yes	9	nmod	_	TokenRange=84:89
11	News	News	X	F%-------------	Foreign=Yes	10	flat:foreign	_	TokenRange=90:94
12	od	od	ADP	RR--2----------	AdpType=Prep|Case=Gen	14	case	_	TokenRange=95:97
13	minulého	minulý	ADJ	AAIS2----1A----	Animacy=Inan|Case=Gen|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos	14	amod	_	TokenRange=98:106
14	týdne	týden	NOUN	NNIS2-----A----	Animacy=Inan|Case=Gen|Gender=Masc|Number=Sing	15	obl	_	TokenRange=107:112
15	posílilo	posílit	VERB	VpNS----R-AAP--	Aspect=Perf|Gender=Neut|Number=Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act	0	root	_	TokenRange=113:121
16	zhruba	zhruba	ADV	Db-------------	_	19	advmod:emph	_	TokenRange=122:128
17	o	o	ADP	RR--4----------	AdpType=Prep|Case=Acc	19	case	_	TokenRange=129:130
18	procentní	procentní	ADJ	AAIS4----1A----	Animacy=Inan|Case=Acc|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos	19	amod	_	TokenRange=131:140
19	bod	bod	NOUN	NNIS4-----A----	Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing	15	obl	_	TokenRange=141:144
20	na	na	ADP	RR--4----------	AdpType=Prep|Case=Acc	24	case	_	TokenRange=145:147
21	31	31	NUM	C=-------------	NumForm=Digit|NumType=Card	24	nummod:gov	_	SpaceAfter=No|TokenRange=148:150
22	,	,	PUNCT	Z:-------------	_	21	punct	_	SpaceAfter=No|TokenRange=150:151
23	2	2	NUM	C=-------------	NumForm=Digit|NumType=Card	21	conj	_	TokenRange=151:152
24	procenta	procento	NOUN	NNNS2-----A----	Case=Gen|Gender=Neut|Number=Sing	15	obl:arg	_	SpaceAfter=No|TokenRange=153:161
25	.	.	PUNCT	Z:-------------	_	15	punct	_	TokenRange=161:162

# sent_id = 3
# text = Koalice Spolu naopak o necelý bod oslabila na 21,6 procenta.
1	Koalice	koalice	NOUN	NNFS1-----A----	Case=Nom|Gender=Fem|Number=Sing	7	nsubj	_	TokenRange=163:170
2	Spolu	spolu	ADV	Db-------------	_	1	advmod	_	TokenRange=171:176
3	naopak	naopak	ADV	Db-------------	_	7	advmod	_	TokenRange=177:183
4	o	o	ADP	RR--4----------	AdpType=Prep|Case=Acc	6	case	_	TokenRange=184:185
5	necelý	celý	ADJ	AAIS4----1N----	Animacy=Inan|Case=Acc|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Neg	6	amod	_	TokenRange=186:192
6	bod	bod	NOUN	NNIS4-----A----	Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing	7	obl	_	TokenRange=193:196
7	oslabila	oslabit	VERB	VpQW----R-AAP--	Aspect=Perf|Gender=Fem,Neut|Number=Plur,Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act	0	root	_	TokenRange=197:205
8	na	na	ADP	RR--4----------	AdpType=Prep|Case=Acc	12	case	_	TokenRange=206:208
9	21	21	NUM	C=-------------	NumForm=Digit|NumType=Card	12	nummod:gov	_	SpaceAfter=No|TokenRange=209:211
10	,	,	PUNCT	Z:-------------	_	11	punct	_	SpaceAfter=No|TokenRange=211:212
11	6	6	NUM	C=-------------	NumForm=Digit|NumType=Card	9	conj	_	TokenRange=212:213
12	procenta	procento	NOUN	NNNS2-----A----	Case=Gen|Gender=Neut|Number=Sing	7	obl	_	SpaceAfter=No|TokenRange=214:222
13	.	.	PUNCT	Z:-------------	_	7	punct	_	TokenRange=222:223

# sent_id = 4
# text = Průzkum se uskutečnil na začátku června, mohla se do něj tedy už promítnout bitcoinová kauza.
1	Průzkum	průzkum	NOUN	NNIS1-----A----	Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing	3	nsubj:pass	_	TokenRange=224:231
2	se	se	PRON	P7-X4----------	Case=Acc|PronType=Prs|Reflex=Yes|Variant=Short	3	expl:pass	_	TokenRange=232:234
3	uskutečnil	uskutečnit	VERB	VpYS----R-AAP--	Aspect=Perf|Gender=Masc|Number=Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act	0	root	_	TokenRange=235:245
4	na	na	ADP	RR--6----------	AdpType=Prep|Case=Loc	5	case	_	TokenRange=246:248
5	začátku	začátek	NOUN	NNIS6-----A----	Animacy=Inan|Case=Loc|Gender=Masc|Number=Sing	3	obl	_	TokenRange=249:256
6	června	červen	NOUN	NNIS2-----A----	Animacy=Inan|Case=Gen|Gender=Masc|Number=Sing	5	nmod	_	SpaceAfter=No|TokenRange=257:263
7	,	,	PUNCT	Z:-------------	_	8	punct	_	TokenRange=263:264
8	mohla	moci	VERB	VpQW----R-AAI--	Aspect=Imp|Gender=Fem,Neut|Number=Plur,Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act	3	conj	_	TokenRange=265:270
9	se	se	PRON	P7-X4----------	Case=Acc|PronType=Prs|Reflex=Yes|Variant=Short	14	expl:pv	_	TokenRange=271:273
10	do	do	ADP	RR--2----------	AdpType=Prep|Case=Gen	11	case	_	TokenRange=274:276
11	něj	on	PRON	PEZS2--3-------	Case=Gen|Gender=Masc,Neut|Number=Sing|Person=3|PrepCase=Pre|PronType=Prs	14	obl	_	TokenRange=277:280
12	tedy	tedy	CCONJ	J^-------------	_	8	cc	_	TokenRange=281:285
13	už	už	ADV	Db-------------	_	14	advmod	_	TokenRange=286:288
14	promítnout	promítnout	VERB	Vf--------A-P--	Aspect=Perf|Polarity=Pos|VerbForm=Inf	8	xcomp	_	TokenRange=289:299
15	bitcoinová	bitcoinový	ADJ	AAFS1----1A----	Case=Nom|Degree=Pos|Gender=Fem|Number=Sing|Polarity=Pos	16	amod	_	TokenRange=300:310
16	kauza	kauza	NOUN	NNFS1-----A----	Case=Nom|Gender=Fem|Number=Sing	8	nsubj	_	SpaceAfter=No|TokenRange=311:316
17	.	.	PUNCT	Z:-------------	_	3	punct	_	TokenRange=316:317

# sent_id = 5
# text = Plný dopad se ale teprve ukáže.
1	Plný	plný	ADJ	AAIS1----1A----	Animacy=Inan|Case=Nom|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos	2	amod	_	TokenRange=318:322
2	dopad	dopad	NOUN	NNIS1-----A----	Animacy=Inan|Case=Nom|Gender=Masc|Number=Sing	6	nsubj:pass	_	TokenRange=323:328
3	se	se	PRON	P7-X4----------	Case=Acc|PronType=Prs|Reflex=Yes|Variant=Short	6	expl:pass	_	TokenRange=329:331
4	ale	ale	CCONJ	J^-------------	_	6	cc	_	TokenRange=332:335
5	teprve	teprve	ADV	Db-------------	_	6	advmod	_	TokenRange=336:342
6	ukáže	ukázat	VERB	VB-S---3P-AAP--	Aspect=Perf|Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin|Voice=Act	0	root	_	SpaceAfter=No|TokenRange=343:348
7	.	.	PUNCT	Z:-------------	_	6	punct	_	SpacesAfter=\n|TokenRange=348:349

# sent_id = 6
# text = ČTK/Red Publikováno 16/06/2025
1	ČTK	ČTK	PROPN	BNXXX-----A----	Abbr=Yes|NameType=Oth	0	root	_	SpaceAfter=No|TokenRange=350:353
2	/	/	PUNCT	Z:-------------	_	3	punct	_	SpaceAfter=No|TokenRange=353:354
3	Red	Red	X	F%-------------	Foreign=Yes	1	conj	_	SpacesAfter=\n|TokenRange=354:357
4	Publikováno	publikovaný	ADJ	VsNS----X-APB--	Foreign=Yes	1	conj	_	TokenRange=358:369
5	16	16	NUM	C=-------------	NumForm=Digit|NumType=Card	1	dep	_	SpaceAfter=No|TokenRange=370:372
6	/	/	PUNCT	Z:-------------	_	7	punct	_	SpaceAfter=No|TokenRange=372:373
7	06	06	NUM	C=-------------	NumForm=Digit|NumType=Card	5	compound	_	SpaceAfter=No|TokenRange=373:375
8	/	/	PUNCT	Z:-------------	_	9	punct	_	SpaceAfter=No|TokenRange=375:376
9	2025	2025	NUM	C=-------------	NumForm=Digit|NumType=Card	5	conj	_	SpacesAfter=\n|TokenRange=376:380

# sent_id = 7
# text = Doba čtení 2 min.
1	Doba	doba	NOUN	NNFS1-----A----	Case=Nom|Gender=Fem|Number=Sing	0	root	_	TokenRange=381:385
2	čtení	čtení	NOUN	NNNS2-----A----	Case=Gen|Gender=Neut|Number=Sing|VerbForm=Vnoun	1	nmod	_	TokenRange=386:391
3	2	2	NUM	C=-------------	NumForm=Digit|NumType=Card	4	nummod	_	TokenRange=392:393
4	min	minuta	NOUN	NNFXX-----A---a	Abbr=Yes|Gender=Fem	1	nmod	_	SpaceAfter=No|TokenRange=394:397
5	.	.	PUNCT	Z:-------------	_	1	punct	_	SpaceAfter=No|TokenRange=397:398
```

Example response
```
{
  "colors": {
    "1": "#6d6df7",
    "2": "#6d7ef7",
    "3": "#6d8ff7",
    "4": "#6da0f7",
    "5": "#6db2f7",
    "6": "#6dc3f7",
    "7": "#6dd4f7",
    "8": "#6de6f7",
    "9": "#6df7f7",
    "10": "#6df7b2",
    "11": "#6df76d",
    "12": "#b2f76d",
    "13": "#f7f76d",
    "14": "#f7d46d",
    "15": "#f7b26d",
    "16": "#f76d6d"
  },
  "result": "# generator = UDPipe 2, https://lindat.mff.cuni.cz/services/udpipe\n# udpipe_model = czech-pdt-ud-2.15-241121\n# udpipe_model_licence = CC BY-NC-SA\n# newdoc\n# newpar\n# sent_id = 1\n# text = STEM: ANO posiluje, Spolu klesá\n1\tSTEM\tSTEM\tNOUN\tBNXXX-----A----\tAbbr=Yes\t0\troot\t_\tSpaceAfter=No|TokenRange=0:4\n2\t:\t:\tPUNCT\tZ:-------------\t_\t4\tpunct\t_\tTokenRange=4:5|PonkApp2:Surprisal=5|PonkApp2:Prob=0.01008|PonkApp2:VocabRank=15\n3\tANO\tANO\tPROPN\tBNXXX-----A----\tAbbr=Yes\t4\tnsubj\t_\tTokenRange=6:9|PonkApp2:Surprisal=12|PonkApp2:Prob=0.00024|PonkApp2:VocabRank=606\n4\tposiluje\tposilovat\tVERB\tVB-S---3P-AAI--\tAspect=Imp|Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin|Voice=Act\t1\tappos\t_\tSpaceAfter=No|TokenRange=10:18|PonkApp2:Surprisal=13|PonkApp2:Prob=0.00001|PonkApp2:VocabRank=4265\n5\t,\t,\tPUNCT\tZ:-------------\t_\t7\tpunct\t_\tTokenRange=18:19|PonkApp2:Surprisal=1|PonkApp2:Prob=0.06026|PonkApp2:VocabRank=1\n6\tSpolu\tspolu\tADV\tDb-------------\t_\t7\tadvmod\t_\tTokenRange=20:25|PonkApp2:Surprisal=12|PonkApp2:Prob=0.00012|PonkApp2:VocabRank=699\n7\tklesá\tklesat\tVERB\tVB-S---3P-AAI--\tAspect=Imp|Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin|Voice=Act\t4\tconj\t_\tSpacesAfter=\\n\\n|TokenRange=26:31|PonkApp2:Surprisal=6|PonkApp2:Prob=0.01166|PonkApp2:VocabRank=16\n\n# newpar\n# sent_id = 2\n# text = Hnutí ANO ve volebním modelu agentury STEM pro CNN Prima News od minulého týdne posílilo zhruba o procentní bod na 31,2 procenta.\n1\tHnutí\thnutí\tNOUN\tNNNS1-----A----\tCase=Nom|Gender=Neut|Number=Sing|VerbForm=Vnoun\t15\tnsubj\t_\tTokenRange=33:38|PonkApp2:Surprisal=10|PonkApp2:Prob=0.00020|PonkApp2:VocabRank=175\n2\tANO\tANO\tPROPN\tBNXXX-----A----\tAbbr=Yes\t1\tnmod\t_\tTokenRange=39:42|PonkApp2:Surprisal=1|PonkApp2:Prob=0.96426|PonkApp2:VocabRank=1\n3\tve\tv\tADP\tRV--6----------\tAdpType=Voc|Case=Loc\t5\tcase\t_\tTokenRange=43:45|PonkApp2:Surprisal=6|PonkApp2:Prob=0.00752|PonkApp2:VocabRank=22\n4\tvolebním\tvolební\tADJ\tAAIS6----1A----\tAnimacy=Inan|Case=Loc|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos\t5\tamod\t_\tTokenRange=46:54|PonkApp2:Surprisal=1|PonkApp2:Prob=0.38122|PonkApp2:VocabRank=1\n5\tmodelu\tmodel\tNOUN\tNNIS6-----A----\tAnimacy=Inan|Case=Loc|Gender=Masc|Number=Sing\t1\tnmod\t_\tTokenRange=55:61|PonkApp2:Surprisal=1|PonkApp2:Prob=0.96094|PonkApp2:VocabRank=1\n6\tagentury\tagentura\tNOUN\tNNFS2-----A----\tCase=Gen|Gender=Fem|Number=Sing\t5\tnmod\t_\tTokenRange=62:70|PonkApp2:Surprisal=1|PonkApp2:Prob=0.19507|PonkApp2:VocabRank=1\n7\tSTEM\tSTEM\tNOUN\tBNXXX-----A----\tAbbr=Yes\t6\tnmod\t_\tTokenRange=71:75|PonkApp2:Surprisal=2|PonkApp2:Prob=0.17558|PonkApp2:VocabRank=2\n8\tpro\tpro\tADP\tRR--4----------\tAdpType=Prep|Case=Acc\t9\tcase\t_\tTokenRange=76:79|PonkApp2:Surprisal=5|PonkApp2:Prob=0.01395|PonkApp2:VocabRank=11\n9\tCNN\tCNN\tPROPN\tBNXXX-----A----\tAbbr=Yes|NameType=Oth\t6\tnmod\t_\tTokenRange=80:83|PonkApp2:Surprisal=1|PonkApp2:Prob=0.31016|PonkApp2:VocabRank=1\n10\tPrima\tPrima\tX\tF%-------------\tForeign=Yes\t9\tnmod\t_\tTokenRange=84:89|PonkApp2:Surprisal=1|PonkApp2:Prob=0.99725|PonkApp2:VocabRank=1\n11\tNews\tNews\tX\tF%-------------\tForeign=Yes\t10\tflat:foreign\t_\tTokenRange=90:94|PonkApp2:Surprisal=1|PonkApp2:Prob=0.52120|PonkApp2:VocabRank=1\n12\tod\tod\tADP\tRR--2----------\tAdpType=Prep|Case=Gen\t14\tcase\t_\tTokenRange=95:97|PonkApp2:Surprisal=6|PonkApp2:Prob=0.00889|PonkApp2:VocabRank=17\n13\tminulého\tminulý\tADJ\tAAIS2----1A----\tAnimacy=Inan|Case=Gen|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos\t14\tamod\t_\tTokenRange=98:106|PonkApp2:Surprisal=2|PonkApp2:Prob=0.10763|PonkApp2:VocabRank=2\n14\ttýdne\ttýden\tNOUN\tNNIS2-----A----\tAnimacy=Inan|Case=Gen|Gender=Masc|Number=Sing\t15\tobl\t_\tTokenRange=107:112|PonkApp2:Surprisal=1|PonkApp2:Prob=0.25745|PonkApp2:VocabRank=1\n15\tposílilo\tposílit\tVERB\tVpNS----R-AAP--\tAspect=Perf|Gender=Neut|Number=Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act\t0\troot\t_\tTokenRange=113:121|PonkApp2:Surprisal=2|PonkApp2:Prob=0.64358|PonkApp2:VocabRank=2\n16\tzhruba\tzhruba\tADV\tDb-------------\t_\t19\tadvmod:emph\t_\tTokenRange=122:128|PonkApp2:Surprisal=4|PonkApp2:Prob=0.01523|PonkApp2:VocabRank=8\n17\to\to\tADP\tRR--4----------\tAdpType=Prep|Case=Acc\t19\tcase\t_\tTokenRange=129:130|PonkApp2:Surprisal=1|PonkApp2:Prob=0.96313|PonkApp2:VocabRank=1\n18\tprocentní\tprocentní\tADJ\tAAIS4----1A----\tAnimacy=Inan|Case=Acc|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos\t19\tamod\t_\tTokenRange=131:140|PonkApp2:Surprisal=5|PonkApp2:Prob=0.01217|PonkApp2:VocabRank=14\n19\tbod\tbod\tNOUN\tNNIS4-----A----\tAnimacy=Inan|Case=Acc|Gender=Masc|Number=Sing\t15\tobl\t_\tTokenRange=141:144|PonkApp2:Surprisal=1|PonkApp2:Prob=0.99496|PonkApp2:VocabRank=1\n20\tna\tna\tADP\tRR--4----------\tAdpType=Prep|Case=Acc\t24\tcase\t_\tTokenRange=145:147|PonkApp2:Surprisal=1|PonkApp2:Prob=0.43112|PonkApp2:VocabRank=1\n21\t31\t31\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t24\tnummod:gov\t_\tSpaceAfter=No|TokenRange=148:150|PonkApp2:Surprisal=3|PonkApp2:Prob=0.10696|PonkApp2:VocabRank=4\n22\t,\t,\tPUNCT\tZ:-------------\t_\t21\tpunct\t_\tSpaceAfter=No|TokenRange=150:151\n23\t2\t2\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t21\tconj\t_\tTokenRange=151:152\n24\tprocenta\tprocento\tNOUN\tNNNS2-----A----\tCase=Gen|Gender=Neut|Number=Sing\t15\tobl:arg\t_\tSpaceAfter=No|TokenRange=153:161|PonkApp2:Surprisal=1|PonkApp2:Prob=0.84859|PonkApp2:VocabRank=1\n25\t.\t.\tPUNCT\tZ:-------------\t_\t15\tpunct\t_\tTokenRange=161:162|PonkApp2:Surprisal=1|PonkApp2:Prob=0.63345|PonkApp2:VocabRank=1\n\n# sent_id = 3\n# text = Koalice Spolu naopak o necelý bod oslabila na 21,6 procenta.\n1\tKoalice\tkoalice\tNOUN\tNNFS1-----A----\tCase=Nom|Gender=Fem|Number=Sing\t7\tnsubj\t_\tTokenRange=163:170|PonkApp2:Surprisal=2|PonkApp2:Prob=0.02918|PonkApp2:VocabRank=3\n2\tSpolu\tspolu\tADV\tDb-------------\t_\t1\tadvmod\t_\tTokenRange=171:176|PonkApp2:Surprisal=1|PonkApp2:Prob=0.87503|PonkApp2:VocabRank=1\n3\tnaopak\tnaopak\tADV\tDb-------------\t_\t7\tadvmod\t_\tTokenRange=177:183|PonkApp2:Surprisal=3|PonkApp2:Prob=0.13362|PonkApp2:VocabRank=4\n4\to\to\tADP\tRR--4----------\tAdpType=Prep|Case=Acc\t6\tcase\t_\tTokenRange=184:185|PonkApp2:Surprisal=2|PonkApp2:Prob=0.16236|PonkApp2:VocabRank=2\n5\tnecelý\tcelý\tADJ\tAAIS4----1N----\tAnimacy=Inan|Case=Acc|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Neg\t6\tamod\t_\tTokenRange=186:192|PonkApp2:Surprisal=6|PonkApp2:Prob=0.00310|PonkApp2:VocabRank=25\n6\tbod\tbod\tNOUN\tNNIS4-----A----\tAnimacy=Inan|Case=Acc|Gender=Masc|Number=Sing\t7\tobl\t_\tTokenRange=193:196|PonkApp2:Surprisal=2|PonkApp2:Prob=0.02459|PonkApp2:VocabRank=2\n7\toslabila\toslabit\tVERB\tVpQW----R-AAP--\tAspect=Perf|Gender=Fem,Neut|Number=Plur,Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act\t0\troot\t_\tTokenRange=197:205|PonkApp2:Surprisal=2|PonkApp2:Prob=0.24860|PonkApp2:VocabRank=2\n8\tna\tna\tADP\tRR--4----------\tAdpType=Prep|Case=Acc\t12\tcase\t_\tTokenRange=206:208|PonkApp2:Surprisal=1|PonkApp2:Prob=0.46886|PonkApp2:VocabRank=1\n9\t21\t21\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t12\tnummod:gov\t_\tSpaceAfter=No|TokenRange=209:211|PonkApp2:Surprisal=2|PonkApp2:Prob=0.10654|PonkApp2:VocabRank=2\n10\t,\t,\tPUNCT\tZ:-------------\t_\t11\tpunct\t_\tSpaceAfter=No|TokenRange=211:212\n11\t6\t6\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t9\tconj\t_\tTokenRange=212:213\n12\tprocenta\tprocento\tNOUN\tNNNS2-----A----\tCase=Gen|Gender=Neut|Number=Sing\t7\tobl\t_\tSpaceAfter=No|TokenRange=214:222|PonkApp2:Surprisal=1|PonkApp2:Prob=0.98147|PonkApp2:VocabRank=1\n13\t.\t.\tPUNCT\tZ:-------------\t_\t7\tpunct\t_\tTokenRange=222:223|PonkApp2:Surprisal=1|PonkApp2:Prob=0.69089|PonkApp2:VocabRank=1\n\n# sent_id = 4\n# text = Průzkum se uskutečnil na začátku června, mohla se do něj tedy už promítnout bitcoinová kauza.\n1\tPrůzkum\tprůzkum\tNOUN\tNNIS1-----A----\tAnimacy=Inan|Case=Nom|Gender=Masc|Number=Sing\t3\tnsubj:pass\t_\tTokenRange=224:231|PonkApp2:Surprisal=8|PonkApp2:Prob=0.00240|PonkApp2:VocabRank=59\n2\tse\tse\tPRON\tP7-X4----------\tCase=Acc|PronType=Prs|Reflex=Yes|Variant=Short\t3\texpl:pass\t_\tTokenRange=232:234|PonkApp2:Surprisal=1|PonkApp2:Prob=0.42601|PonkApp2:VocabRank=1\n3\tuskutečnil\tuskutečnit\tVERB\tVpYS----R-AAP--\tAspect=Perf|Gender=Masc|Number=Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act\t0\troot\t_\tTokenRange=235:245|PonkApp2:Surprisal=2|PonkApp2:Prob=0.46744|PonkApp2:VocabRank=2\n4\tna\tna\tADP\tRR--6----------\tAdpType=Prep|Case=Loc\t5\tcase\t_\tTokenRange=246:248|PonkApp2:Surprisal=3|PonkApp2:Prob=0.04431|PonkApp2:VocabRank=5\n5\tzačátku\tzačátek\tNOUN\tNNIS6-----A----\tAnimacy=Inan|Case=Loc|Gender=Masc|Number=Sing\t3\tobl\t_\tTokenRange=249:256|PonkApp2:Surprisal=2|PonkApp2:Prob=0.12117|PonkApp2:VocabRank=2\n6\tčervna\tčerven\tNOUN\tNNIS2-----A----\tAnimacy=Inan|Case=Gen|Gender=Masc|Number=Sing\t5\tnmod\t_\tSpaceAfter=No|TokenRange=257:263|PonkApp2:Surprisal=4|PonkApp2:Prob=0.06633|PonkApp2:VocabRank=8\n7\t,\t,\tPUNCT\tZ:-------------\t_\t8\tpunct\t_\tTokenRange=263:264|PonkApp2:Surprisal=2|PonkApp2:Prob=0.17113|PonkApp2:VocabRank=3\n8\tmohla\tmoci\tVERB\tVpQW----R-AAI--\tAspect=Imp|Gender=Fem,Neut|Number=Plur,Sing|Polarity=Pos|Tense=Past|VerbForm=Part|Voice=Act\t3\tconj\t_\tTokenRange=265:270|PonkApp2:Surprisal=12|PonkApp2:Prob=0.00001|PonkApp2:VocabRank=695\n9\tse\tse\tPRON\tP7-X4----------\tCase=Acc|PronType=Prs|Reflex=Yes|Variant=Short\t14\texpl:pv\t_\tTokenRange=271:273|PonkApp2:Surprisal=1|PonkApp2:Prob=0.32388|PonkApp2:VocabRank=1\n10\tdo\tdo\tADP\tRR--2----------\tAdpType=Prep|Case=Gen\t11\tcase\t_\tTokenRange=274:276|PonkApp2:Surprisal=1|PonkApp2:Prob=0.32391|PonkApp2:VocabRank=1\n11\tněj\ton\tPRON\tPEZS2--3-------\tCase=Gen|Gender=Masc,Neut|Number=Sing|Person=3|PrepCase=Pre|PronType=Prs\t14\tobl\t_\tTokenRange=277:280|PonkApp2:Surprisal=1|PonkApp2:Prob=0.97808|PonkApp2:VocabRank=1\n12\ttedy\ttedy\tCCONJ\tJ^-------------\t_\t8\tcc\t_\tTokenRange=281:285|PonkApp2:Surprisal=2|PonkApp2:Prob=0.22033|PonkApp2:VocabRank=2\n13\tuž\tuž\tADV\tDb-------------\t_\t14\tadvmod\t_\tTokenRange=286:288|PonkApp2:Surprisal=3|PonkApp2:Prob=0.00718|PonkApp2:VocabRank=5\n14\tpromítnout\tpromítnout\tVERB\tVf--------A-P--\tAspect=Perf|Polarity=Pos|VerbForm=Inf\t8\txcomp\t_\tTokenRange=289:299|PonkApp2:Surprisal=2|PonkApp2:Prob=0.84488|PonkApp2:VocabRank=2\n15\tbitcoinová\tbitcoinový\tADJ\tAAFS1----1A----\tCase=Nom|Degree=Pos|Gender=Fem|Number=Sing|Polarity=Pos\t16\tamod\t_\tTokenRange=300:310|PonkApp2:Surprisal=11|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=269\n16\tkauza\tkauza\tNOUN\tNNFS1-----A----\tCase=Nom|Gender=Fem|Number=Sing\t8\tnsubj\t_\tSpaceAfter=No|TokenRange=311:316|PonkApp2:Surprisal=2|PonkApp2:Prob=0.11421|PonkApp2:VocabRank=3\n17\t.\t.\tPUNCT\tZ:-------------\t_\t3\tpunct\t_\tTokenRange=316:317|PonkApp2:Surprisal=2|PonkApp2:Prob=0.13357|PonkApp2:VocabRank=3\n\n# sent_id = 5\n# text = Plný dopad se ale teprve ukáže.\n1\tPlný\tplný\tADJ\tAAIS1----1A----\tAnimacy=Inan|Case=Nom|Degree=Pos|Gender=Masc|Number=Sing|Polarity=Pos\t2\tamod\t_\tTokenRange=318:322|PonkApp2:Surprisal=13|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=3646\n2\tdopad\tdopad\tNOUN\tNNIS1-----A----\tAnimacy=Inan|Case=Nom|Gender=Masc|Number=Sing\t6\tnsubj:pass\t_\tTokenRange=323:328|PonkApp2:Surprisal=4|PonkApp2:Prob=0.01221|PonkApp2:VocabRank=10\n3\tse\tse\tPRON\tP7-X4----------\tCase=Acc|PronType=Prs|Reflex=Yes|Variant=Short\t6\texpl:pass\t_\tTokenRange=329:331|PonkApp2:Surprisal=4|PonkApp2:Prob=0.01930|PonkApp2:VocabRank=8\n4\tale\tale\tCCONJ\tJ^-------------\t_\t6\tcc\t_\tTokenRange=332:335|PonkApp2:Surprisal=1|PonkApp2:Prob=0.30319|PonkApp2:VocabRank=1\n5\tteprve\tteprve\tADV\tDb-------------\t_\t6\tadvmod\t_\tTokenRange=336:342|PonkApp2:Surprisal=2|PonkApp2:Prob=0.20917|PonkApp2:VocabRank=2\n6\tukáže\tukázat\tVERB\tVB-S---3P-AAP--\tAspect=Perf|Mood=Ind|Number=Sing|Person=3|Polarity=Pos|Tense=Pres|VerbForm=Fin|Voice=Act\t0\troot\t_\tSpaceAfter=No|TokenRange=343:348|PonkApp2:Surprisal=1|PonkApp2:Prob=0.38604|PonkApp2:VocabRank=1\n7\t.\t.\tPUNCT\tZ:-------------\t_\t6\tpunct\t_\tSpacesAfter=\\n|TokenRange=348:349|PonkApp2:Surprisal=1|PonkApp2:Prob=0.69173|PonkApp2:VocabRank=1\n\n# sent_id = 6\n# text = ČTK/Red Publikováno 16/06/2025\n1\tČTK\tČTK\tPROPN\tBNXXX-----A----\tAbbr=Yes|NameType=Oth\t0\troot\t_\tSpaceAfter=No|TokenRange=350:353\n2\t/\t/\tPUNCT\tZ:-------------\t_\t3\tpunct\t_\tSpaceAfter=No|TokenRange=353:354\n3\tRed\tRed\tX\tF%-------------\tForeign=Yes\t1\tconj\t_\tSpacesAfter=\\n|TokenRange=354:357\n4\tPublikováno\tpublikovaný\tADJ\tVsNS----X-APB--\tForeign=Yes\t1\tconj\t_\tTokenRange=358:369\n5\t16\t16\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t1\tdep\t_\tSpaceAfter=No|TokenRange=370:372\n6\t/\t/\tPUNCT\tZ:-------------\t_\t7\tpunct\t_\tSpaceAfter=No|TokenRange=372:373\n7\t06\t06\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t5\tcompound\t_\tSpaceAfter=No|TokenRange=373:375\n8\t/\t/\tPUNCT\tZ:-------------\t_\t9\tpunct\t_\tSpaceAfter=No|TokenRange=375:376\n9\t2025\t2025\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t5\tconj\t_\tSpacesAfter=\\n|TokenRange=376:380\n\n# sent_id = 7\n# text = Doba čtení 2 min.\n1\tDoba\tdoba\tNOUN\tNNFS1-----A----\tCase=Nom|Gender=Fem|Number=Sing\t0\troot\t_\tTokenRange=381:385\n2\tčtení\tčtení\tNOUN\tNNNS2-----A----\tCase=Gen|Gender=Neut|Number=Sing|VerbForm=Vnoun\t1\tnmod\t_\tTokenRange=386:391\n3\t2\t2\tNUM\tC=-------------\tNumForm=Digit|NumType=Card\t4\tnummod\t_\tTokenRange=392:393\n4\tmin\tminuta\tNOUN\tNNFXX-----A---a\tAbbr=Yes|Gender=Fem\t1\tnmod\t_\tSpaceAfter=No|TokenRange=394:397\n5\t.\t.\tPUNCT\tZ:-------------\t_\t1\tpunct\t_\tSpaceAfter=No|TokenRange=397:398\n\n"
}
```
