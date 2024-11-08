
FROM --platform=$BUILDPLATFORM node:14.4.0-alpine AS development

RUN mkdir /project
WORKDIR /project

COPY . .

RUN yarn global add @vue/cli
RUN yarn install
ENV HOST=0.0.0.0
CMD ["yarn", "run", "serve"]

