# Session 56 — Recommender Systems

## Goal

Understand similarity, latent-vector intuition, ranking/prediction objectives, and recommendation evaluation.

## Learn

Connect user/item vectors, dot-product similarity, collaborative filtering intuition, cold-start problems, and the difference between predicting a rating and ranking useful items.

## Practice

- calculate a small dot-product similarity;
- compare nearest/similar items;
- identify leakage risks in random splits when user/time structure matters;
- discuss precision@k/recall@k or task-specific ranking metrics where appropriate.

## Rebuild

Students design a minimal recommendation baseline and validation plan for a small interaction dataset before trying a more complex method.

## Share

Explain one reason a recommender can score well offline but still produce poor or harmful recommendations in practice.

## Evidence

- similarity calculation;
- baseline/validation plan;
- ranking or prediction metric rationale;
- cold-start/feedback-loop limitation.

## Exit Check

Student can explain vector similarity and choose an evaluation split/metric that respects the recommendation task rather than blindly using random row accuracy.
