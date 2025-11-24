---
title: Glitter CLI
nav_order: 4
---

# PONK: Glitter cli
This is command line interface for PONK glitter tool set.

## Usage
Usage scheme:

```bash
glitter_cli.py [-h] [--to-json | --to-html | --to-dict | --to-table | --to-tex] [--output OUTPUT] [--input INPUT] [--model MODEL]
```

### Options
- `-h`, `--help`     - show help massage and exit
- Export formats:
    - `--to-json`    - export data to JSON
    - `--to-html`    - export data to HTML
    - `--to-dict`    - export data to python dictionary format
    - `--to-table`   - export data to table containing for each token, its probability, order and top 10 candidates
    - `--to-tex`     - export data as TeX macros
    - `--to-conllu`  - export data in conllu format for PONK integration
    - Not choosing any export format will result in printing colored glittered text
- `--output OUTPUT`  - output file name (default: `stdout`)
- `--input INPUT`    - input file name (default: `stdin`)
- `--model MODEL`    - name of model you want to use to glitter text (default: `Robeczech`)


## Examples

### Example 1
```bash
cat kabat_kdo_vi_jestli.txt | ./glitter_cli.py --model robeczech --to-table
```
results
```
┏━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Word    ┃  Nth  ┃ Probability ┃                                              Top results ┃
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

