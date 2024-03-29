# installs NVM (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Need to exit and re-enter the shell to use nvm and download and install Node.js
nvm install 21

# verifies the right Node.js version is in the environment
node -v # should print `v21.7.1`

# verifies the right NPM version is in the environment
npm -v # should print `10.5.0`

npm install -g sass
npm install -g typescript