# Entity matching

Much like collecting sports player cards, the great joy of well-defined entity data is to compare entities. Such comparisons can produce investigative leads when cross-referencing a watchlist with a leaked dataset, serve as a risk signal when screening customers against a sanctions list, or be part of a data factory that deduplicates and integrates multiple instances of the same logical entity.

Entity matching is fundamentally about managing a lack of information (if all companies and people in the world were numbered, for example, the issue would not exist). Given that all decisions will be imperfect, entity matching is a matter of trade-offs: precision vs. recall, rule-based vs. statistical, etc. This is why FtM no longer attempts to define a universal method for entity matching. Instead, many systems exist within the ecosystem:

## Tools overview

* `followthemoney.compare`: a basic entity matching tool included in FollowTheMoney. It uses fixed 