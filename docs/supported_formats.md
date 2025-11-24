---
title: Supported formats
nav_order: 7
---

# Supported Formats

### HTML

Simplified output of glittered text with one token `Ivanka`:
```html
<div class="glittered-text">
    <div class="glitter-token">
        <span class="gt-heatmap-15">Ivanka</span>
        <div class="gt-context">
            <span class="gt-probability">P: 0.00000000</span>
            <span class="gt-nth">N: 38220</span>
            <hr>
            <ol>
                <li>[SEP] (0.99999642)</li>
                <li> P (0.00000083)</li>
                <li> V (0.00000025)</li>
                <li>[CLS] (0.00000016)</li>
                <li> Ř (0.00000015)</li>
            </ol>
        </div>
    </div>
</div>
```

### JSON

Simplified output of glittered text with one token `Bára`:
```json
{
  "content": [
    {
      "original_token": "Bára",
      "probability": 3.7422456800051407e-10,
      "nth": 438,
      "top_5": [
        ["[SEP]", 0.9999964237213135],
        [" P", 8.339781629729259e-07],
        [" V", 2.5482094656581467e-07],
        ["[CLS]", 1.5537057151959743e-07],
        [" \u0158", 1.4771539724733884e-07]
      ]
    }
  ],
  "used_models": ["Robeczech"]
}
```

### Python dict

Simplified output of glittered text with one token `Silva`:
```python
{'content': [{
    {'original_token': 'Silva',
     'probability': 7.57262568623629e-12,
     'nth': 3352,
     'top_5': [('[SEP]', 0.9999964237213135),
               (' P', 8.339781629729259e-07),
               (' V', 2.5482094656581467e-07),
               ('[CLS]', 1.5537057151959743e-07),
               (' Ř', 1.4771539724733884e-07)]
    },
 ],
 'used_models': ['Robeczech']
}
```

### CONLLU

```
'Proč'	PonkApp2:Surprisal=15|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=11450
' si'	PonkApp2:Surprisal=13|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=3796
' mat'	PonkApp2:Surprisal=13|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=4392
'fy'	PonkApp2:Surprisal=10|PonkApp2:Prob=0.00001|PonkApp2:VocabRank=185
'zá'	PonkApp2:Surprisal=10|PonkApp2:Prob=0.00006|PonkApp2:VocabRank=147
'ci'	PonkApp2:Surprisal=3|PonkApp2:Prob=0.00088|PonkApp2:VocabRank=4
' p'	PonkApp2:Surprisal=12|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=960
'letou'	PonkApp2:Surprisal=1|PonkApp2:Prob=0.13792|PonkApp2:VocabRank=1
' Hal'	PonkApp2:Surprisal=15|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=11024
'lo'	PonkApp2:Surprisal=2|PonkApp2:Prob=0.04913|PonkApp2:VocabRank=2
'ween'	PonkApp2:Surprisal=2|PonkApp2:Prob=0.09415|PonkApp2:VocabRank=2
' a'	PonkApp2:Surprisal=3|PonkApp2:Prob=0.00035|PonkApp2:VocabRank=4
' Vánoce'	PonkApp2:Surprisal=1|PonkApp2:Prob=0.00154|PonkApp2:VocabRank=1
'?'	PonkApp2:Surprisal=4|PonkApp2:Prob=0.00001|PonkApp2:VocabRank=8
'\n'	PonkApp2:Surprisal=16|PonkApp2:Prob=0.00000|PonkApp2:VocabRank=31104
```
