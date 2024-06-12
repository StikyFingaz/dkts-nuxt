<script setup lang="ts">
const { data: translations } = useNuxtData("aboutStrings");
const { data: actors } = useNuxtData("actorsData");
const displaySize = useState("displaySize");
</script>

<template lang="html">
  <div id="mainRow" class="row justify-content-center">
    <div v-for="actor in actors" class="col-11 col-md-12 col-lg-10 mb-3 card-col">
      <div class="row">
        <div class="col-md-4">
          <ActorCard :nickname="actor.nickname">
            <template #images>
              <!-- <img
                v-if="['xs', 'sm', 'xl', 'xxl'].includes(displaySize)"
                :src="setThumborUrl(`/media/actors/${actor.nickname}/profile.jpg`, 'unsafe/340x0/filters:format(webp)')"
                class="card-img-top img-fluid lazy"
                alt=""
                width="340"
                height="422"
                loading="lazy"
              />
              <img
                v-if="['md', 'lg'].includes(displaySize)"
                :src="setThumborUrl(`/media/actors/${actor.nickname}/profile.jpg`, 'unsafe/225x0/filters:format(webp)')"
                class="card-img-top img-fluid lazy"
                alt=""
                width="225"
                height="279"
                loading="lazy"
              /> -->
              <NuxtImg
                format="webp"
                :src="`/media/actors/${actor.nickname}/profile.jpg`"
                :alt="`Profile - ${actor.name}`"
                class="card-img-top img-fluid"
                width="1040"
                height="1290"
                sizes="320px md:220px lg:240 xl:340 xxl:340"
                :placeholder="[104, 129, 1, 15]"
                loading="lazy"
              />
            </template>
            <template #name>
              {{ getTranslation(actor, "name") }}
            </template>
          </ActorCard>
        </div>
        <div class="col-md-8 row d-none d-md-flex">
          <div class="card-body">
            <h1 class="card-title display-6">{{ getTranslation(actor, "name") }}</h1>
            <span ref="actorBio" id="actorBio">
              <p v-for="p in getTranslation(actor, 'short_bio').split('\n')" class="lead">
                {{ p }}
              </p>
            </span>
          </div>
          <NuxtLinkLocale :to="`/about/actors/${actor.nickname}`" id="readMoreBtn" class="btn btn-dark align-self-end">
            {{ translations.meet }} {{ getTranslation(actor, "name").split(" ")[0] }}
          </NuxtLinkLocale>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped>
#actorBio {
  display: -webkit-box;
  /* -webkit-line-clamp: 5; */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}

#readMoreBtn {
  max-width: max-content;
}

@media (max-width: 1200px) {
  #actorBio {
    -webkit-line-clamp: 5;
  }
}

@media (min-width: 1201px) {
  #actorBio {
    -webkit-line-clamp: 9;
  }
}

p {
  display: inline;
}

p::after {
  content: " \A\A";
  white-space: pre;
}
</style>
