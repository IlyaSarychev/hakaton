FROM node:lts-alpine

RUN npm install -g http-server

ENV DIST_DIR /app
ENV SOURCE_DIR /frontend

WORKDIR $DIST_DIR

COPY ${SOURCE_DIR}/package*.json ${DIST_DIR}/

RUN yarn install

COPY ${SOURCE_DIR}/ ${DIST_DIR}/

RUN yarn run

EXPOSE 8080
CMD [ "http-server", "dist" ]