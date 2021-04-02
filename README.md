pdf файлы некоторых олимпиад, а так же код чтобы скачивать задачи с сайта можно найти [тут](https://github.com/mathogram/kz-olymps).

рекомендую поставить это как katex options
```
const options = {
    "displayMode":false,
    "delimiters":[
        {left: "$$", right: "$$", display: true},
        {left: "$", right: "$", display: false},
		{left: "\\(", right: "\\)", display: false},
		{left: "\\[", right: "\\]", display: true}
    ],
	...
    "macros":{
        "\\Q": "\\mathbb{Q}" ,
        "\\C": "\\mathbb{C}" ,
        "\\P": "\\mathbb{P}" ,
        "\\gcd": "\\textrm{gcd}" ,
        "\\lcm": "\\textrm{lcm}" ,
        "\\mult": "\\thinspace\\raisebox{-0.16em}{$\\vdots$}\\thinspace" ,
        "\\mod": "\\text{\\thinspace(mod } #1)",
        "\\abs": "\\lvert #1 \\rvert",
        "\\displaylines": "#1",
        "\\hbox": "\\text{#1}",
        "\\mathstrut": "#1",
		"&amp;":"&",
		"&gt;":">",
		"&lt;":"<",
		"&le;":"\le",
		"&ge;":"\ge",
    }
}
```
