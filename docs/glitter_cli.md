# PONK: Glitter cli
This is command line interface for PONK glitter tool set.


## Usage
Usage shema:

```bash
glitter_cli.py [-h] [--to-json | --to-html | --to-dict | --to-table] [--output OUTPUT] [--input INPUT] [--model MODEL]
```

### Options
- `-h`, `--help`     - show help massega
- Export formats:
    - `--to-json`    - export data to JSON
    - `--to-html`    - export data to HTML
    - `--to-dict`    - export data to python dictionary format
    - `--to-table`   - export data to table containig token, its probability, order and top 10 candidates
    - Not choosing any export format will result in printing colored glittered text
- `--output OUTPUT`  - output file name (default: `stdout`)
- `--input INPUT`    - input file name (default: `stdin`)
- `--model MODEL`    - name of model you want to use to glitter text (default: `Robeczech`)

## Formats

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
    ], 'used_models': ["Robeczech"]}⏎
```

## Examples

### Example 1
```bash
cat kabat_kdo_vi_jestli.txt | ./glitter_cli.py --model robeczech --to-table
```
prints
```
┏━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Word    ┃  Nth  ┃ Probability ┃                                                   Top 10 ┃
┡━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ [CLS]   │   1   │  0.99972230 │               [CLS] [SEP] ero so min seni um s ště proti │
│ K       │  17   │  0.00000004 │                       [SEP]  P  V [CLS]  Ř  "  I -  B  J │
│ doví    │ 31169 │  0.00000000 │                            [SEP] .  :  ) / FOTO  " ! * B │
│  jestli │  499  │  0.00000133 │                      [SEP] kové ci K cí k ky kam kovi  k │
│  jestli │  106  │  0.00000013 │                    [SEP] .  eu  e  P [CLS]  E  i  K  nep │
│ [\n]    │  244  │  0.00000019 │              [SEP]  eu  e [CLS]  P  kdo .  neví  komu  E │
│ j       │  139  │  0.00000223 │                    [SEP] [CLS]  k  P  K .  kdo  D  i  Ti │
│ sou     │  771  │  0.00001447 │                                [SEP] j - ne . ! k š ? ko │
│  na     │  10   │  0.00023646 │                           [SEP] . ? !  a - ,  nebo j  na │
│  měsíci │ 5614  │  0.00000052 │ [SEP]  mě  kole k n MS  náměstí  světě  stadionu  fotbal │
│ [\n]    │  27   │  0.00006799 │                            [SEP] . ? , !  a  nebo -  - . │
│ vů      │ 23598 │  0.00000001 │                              [SEP] .  “  " ? ! ? .  ) fi │
│ bec     │ 3491  │  0.00000035 │                         [SEP]  K [CLS] V pak ví ? ně ? K │
│         │  526  │  0.00004692 │                               [SEP] . ? - k ! ně K  K ce │
│ ňá      │  16   │  0.00707522 │                                 ů ý ď ňák ^ Ý q @ ním ím │
│ ký      │   1   │  0.12435737 │                      ký kej [SEP] ky ká kam ka ko kým ké │
│  stopy  │ 9013  │  0.00000012 │                            [SEP] . ? ho ! m - mu ,  nebo │
│ [\n]    │  43   │  0.00001084 │                               [SEP] . ? ! , _ ?  :  "  … │
│ a       │  19   │  0.00004312 │                       [SEP]  " . ?  “ ! ?  nebo  tom  co │
│  proč   │  144  │  0.00008828 │                                 [SEP] . ? - ! a _ / , ma │
│  kope   │ 33293 │  0.00000000 │          [SEP] [CLS] dek pak ho ka  jaký  proč Jaký  kde │
│  kolem  │  91   │  0.00000691 │                          [SEP] ? š .  kam j ! chá uje  : │
│ [\n]    │ 4060  │  0.00000051 │            [SEP] ? .  nebe  něj  sebe A  kam  stromů  mě │
│ se      │  188  │  0.00002216 │                            [SEP] . ? ? !  proč ! ho j ne │
│ be      │  148  │  0.00001956 │                            [SEP] ? . ho j  proč _ ka - ! │
│  kdo    │  63   │  0.00018998 │                          [SEP] ? . š be ho -  proč se si │
│  se     │  22   │  0.00028679 │                   [SEP] pak ? má si  má  je  proč ´  kde │
│  topí   │  748  │  0.00002439 │ [SEP]  bojí  ptá že  diví  nebojí  proč  podívá  dívá je │
│ [\n]    │  179  │  0.00000183 │                     [SEP] ? . !  nebo  proč  jak  a  v j │
│ jak     │  11   │  0.00019399 │                        [SEP] . ? ?  “ !  " !  proč  nebo │
│ ej      │   2   │  0.02724240 │                               [SEP] ej o ý ým é á j em e │
│  sval   │ 12403 │  0.00000046 │                       [SEP] [CLS] ho o z mu p dek ka kdo │
│  to     │  715  │  0.00000500 │                  [SEP] ovec . ? ov bák stvo čík ina ovač │
│  zemí   │ 19153 │  0.00000006 │                    [SEP]  je má  má  není  vem ne ně ž k │
│  otá    │ 4744  │  0.00000018 │                              [SEP] . ? ! ne j No m pe má │
│ čí      │   2   │  0.18005991 │                     [SEP] čí lí čej zej zá ček čku pe za │
│ [\n]    │ 1139  │  0.00000011 │             [SEP]  jak  a ?  A j  proč  jestli  co  nebo │
│ [SEP]   │   1   │  0.98804224 │                          [SEP] . ? ? A ! No !  jak  nebo │
└─────────┴───────┴─────────────┴──────────────────────────────────────────────────────────┘
```

### Example 2
```bash
echo "Proč si matfyzáci pletou Halloween a Vánoce? Protože OCT 31 = DEC 25." | ./glitter_cli.py
```
results in
```
[CLS]Proč si matfyzáci pletou Halloween a Vánoce? Protože OCT 31 = DEC 25.[SEP]
```
(this output is colored by glitter but this markdown file can not preserve colored text)

