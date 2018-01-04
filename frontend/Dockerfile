FROM mhart/alpine-node:8.7.0
ARG port=3000
ENV PORT=$port 
# Create app directory
WORKDIR /usr/src/app
# Install app dependencies
COPY package.json yarn.lock index.js ./
COPY ./build ./build
RUN yarn install
# Bundle app source
EXPOSE $port 
CMD [ "yarn", "serve" ]
