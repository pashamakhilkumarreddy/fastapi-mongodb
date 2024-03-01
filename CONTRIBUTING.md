# Contributing

👋 Hello! Thank you for your interest in contributing to the FastAPI project. We welcome contributions from everyone!

## Code Contributions

Please review the [README](./README.md) document for prerequisites and instructions on getting started with FastAPI development.

When creating your Pull Request (PR), follow these steps:

### 📝 Authoring Your PR

-   Ensure your branch is up-to-date with the latest code from the `main` branch. This helps prevent regressions and conflicts.
-   Write your PR title using the semantic commit format. Refer to the [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/#summary) specification for details. A clear title helps reviewers understand the nature of your change.
-   Complete the PR title and description in the pull request template. Assume reviewers lack the context to review your change and provide it in the PR description.
-   The title and description will be used in the changelog and committed to the Git history, so they should be thoughtfully written to provide future maintainers with context, including details on implementation choices.
-   Link to relevant tickets, other PRs, or any other external sources that can provide context for your change. While these sources should not replace a good PR description, feel free to copy and paste relevant context from them.

### Providing Testing Instructions

-   Provide test links and steps to verify the effects of your change. Use our QA tools to show the results of your PR's changes. Include a brief description of what to look for in each link.
-   If you want reviewers to view the code locally, provide necessary links and any additional steps they need to take before reviewing the change (e.g., setting environment variables, running scripts).

### Merging Your PR

-   When merging, copy and paste your PR title as your commit title and the PR description as your commit body. Then merge your change!
-   All merges to `main` are automatically pushed to staging and production. Ensure your work appears as expected in these environments post-deployment.

## Code Review Process Guidelines

### Guidelines for Everyone

-   Approach code reviews positively, aiming to enhance the codebase.
-   Ask good questions without making demands. ("What do you think about naming this `firstName`?")
-   Avoid judgment and assumptions about the author's perspective.
-   Seek clarification when needed. ("I didn't understand. Can you please clarify?")
-   Avoid selective ownership of code. Use inclusive language like "ours" instead of "mine" or "yours".
-   Refrain from using terms that refer to personal traits. Assume everyone is intelligent and well-meaning.
-   Be explicit, as online intentions can be misunderstood.
-   Stay humble. ("I'm not sure - let's look it up.")
-   If there are too many "I didn't understand" or "Alternative solution" comments, discuss synchronously (e.g., chat, screen sharing, in person). Follow up with a comment summarizing the discussion.

### Guidelines for Authors

-   Prefer smaller, focused PRs. Scope your changes to one feature or part of the system. Smaller PRs are easier to review and less prone to regressions. If your PR is large or touches many parts of the codebase, you may be asked to break it into smaller PRs. Work with product and design stakeholders to scope tickets and feedback cycles accordingly.
    -   In some cases, breaking a large PR may introduce more risk or require significantly more work. If unsure, reach out to the team or relevant channels for guidance.
    -   For stakeholder review, consider using discrete commits for each feature or a feature branch that you then create smaller PRs from for developer review.
-   Notify your team when you need a review and be proactive about getting your code merged. Merge your code if it has the necessary approvals. Request reviews from other developers familiar with that part of the codebase if needed.
-   If a reviewer's comments are outside the scope of the PR, consider extracting those changes or suggestions into future tickets instead of overloading a single PR.
-   Review your own code meticulously and test it thoroughly.
-   Be grateful for reviewers' suggestions. ("Good call. I'll make that change.")
-   Welcome all reviews and seek to understand the reviewer's perspective. Different insights can raise points you hadn't considered.
-   Remember, the review is of the code, not you. Be aware of [how hard it is to convey emotion online](https://www.fastcodesign.com/3036748/why-its-so-hard-to-detect-emotion-in-emails-and-texts) and how easy it is to misinterpret feedback. If a review seems aggressive or personal, ask for clarification.
-   Assume the best intention from reviewers' comments.
-   Push commits based on feedback as isolated commits. Do not squash until ready to merge. Reviewers should be able to read updates based on their feedback.
-   Respond to every comment and allow the original commenter to "resolve" the conversation in GitHub.

### Guidelines for Reviewers

-   Understand why the change is necessary (fixes a bug, improves the user experience, refactors existing code). Ask for context if needed.
-   Communicate the strength of your ideas. Make it clear which changes are blocking and which are suggestions.
-   Prefix comments with guideposts to indicate importance (e.g., `Nit: this variable name seems too generic`, `Blocking: if the input is x, this will fail`).
-   Prioritize bugs, tests, and code quality over subjective aspects like coding style.
-   Identify ways to simplify the code while still solving the problem.
-   Offer alternative implementations but assume the author has considered them. ("What do you think about using a custom validator here?")
-   Seek to understand the author's perspective.
-   Ask for additional reviews if unsure.
-   Run changes locally or in a staging environment to confirm everything works as expected.