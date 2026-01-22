# Trustable Compliance Report



## Item status guide ## { .subsection }

Each item in a Trustable Graph is scored with a number between 0 and 1.
The score represents aggregated organizational confidence in a given Statement, with larger numbers corresponding to higher confidence.
Scores in the report are indicated by both a numerical score and the colormap below:
<div class="br" style="height: 26px; width: 80%;background: linear-gradient(to right in hsl, hsl(0.0, 100%, 65%) 0%, hsl(120.0, 100%, 30%) 100%);">
<span style="float:right;">1.00&nbsp</span>
<span style="float:left;">&nbsp0.00</span>
</div>


The status of an item and its links also affect the score.

Unreviewed items are indicated by a cross in the status column.
The score of unreviewed items is always set to zero.


Suspect links are indicated by a cross in the status column.
The contribution to the score of a parent item by a suspiciously linked child is always zero, regardless of the child's own score.
## Compliance for HELLO ## {: data-toc-label="HELLO"}

| Item {style="width:15%"} | Summary {style="width:55%"} | Score {style="width:0%"} | Score Origin {style="width:5%"} | Status {style="width:25%"} |
| --- | --- | --- | --- | --- |
| [HELLO-BIN](HELLO.md#hello-bin) {class="tsf-score" style="background-color:hsl(108.0, 100%, 33%)"} | Hello builds as expected | 0.90 | SME with References and Validator | ✔ Item Reviewed<br>✔ All Children Linked |


---

_Generated for: Software_

* _Repository root: /var/home/lrossett/tmp/tsf/hello-world_
