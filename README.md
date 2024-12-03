# GitHub Demo for Penta

### Build and run app in remote dev environment - Codespaces
1. Open repo in browser and open Codespaces to get remote working developer machine
2. Open ```src/demoapp/main.py```
2. Run it using preconfigured task -> CTRL+SHIFT+P, Run Task, select ```Run Demo App```
3. Pop-up will show to open app in browser

### Push, build and deploy to serverless container platform - Azure Container Apps
1. Go to GitHub Action and run ```Build and deploy demo app``` pipeline to build container and deploy to Azure Container App
2. Open Azure Portal, find Azure Container App and access the app

### Use AI to enhance your code - GitHub Copilot
1. Note I can select various AI engines even from different vendors
2. Keep you main.py open and ask copilot to add comments and docstrings to your code ```Add comments or docstrings to my file to enhance readability.```
3. Let Copilot explain part of code by selecting it and asking in context of whole workspace with ```@workspace /explain```
4. Generate tests with ```@workspace /tests```
5. Go to multi-file edit, move all files of demoapp to context and enhance app with: ```Now add another company: Prima Banka. Graph should show how are users satisfied with GitHub with 90% very satisfied, 8% satisfied and 2% not sure.```
6. Try app, commit (let Copilot write message for you) and push changes to automatically deploy to Azure

### Use extensions
1. Ask about your Azure: ```@azure /resources Do I have any Azure Container Apps deployed?```
2. Learn about Azure, troubleshoot: ```@azure /help I have created NSG to filter traffic, but it is still passing.```
3. Investigate costs: ```@azure /costs What can you tell me about storage costs im my subscription 673af34d-6b28-41dc-bc7b-f507418045e6```

### Advanced AI with Copilot Workspace, agents and Advanced Security
1. Showcase "Review and Comment" in VS Code and explain how it will be agentic in CI/CD
2. In GitHub discuss Dependabot and its importance for security. Showcase automated PRs to fix problems.
3. In GitHub check Security issues, get some and use Copilot to generate code to fix them.
4. Show next-gen prototype of [Copilot Workspace](https://copilot-workspace.githubnext.com/). First brainstorm, add few ideas and than generate plan. Afterward we can generate code for it.


