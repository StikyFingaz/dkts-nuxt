<script setup lang="ts">
const route = useRoute();
const { data: translations } = useNuxtData("aboutStrings");
const { data: actor } = useNuxtData(route.params.nickname);

const shortBio = ref(null);
const isTruncated = ref(false);

onMounted(() => {
  const descriptionElement = shortBio.value;
  const clientHeight = descriptionElement.clientHeight;
  const scrollHeight = descriptionElement.scrollHeight;

  isTruncated.value = clientHeight < scrollHeight;
});
</script>

<template lang="html">
  <div v-if="actor" id="idContainer" class="container d-flex align-items-center mt-3 mt-lg-2 mb-3 mb-lg-2">
    <div id="actorCard" class="card col-12" data-bs-theme="light">
      <div class="card-header d-flex justify-content-between align-items-center">
        <h1 id="actorName" class="display-5 text-uppercase mb-0">
          {{ getTranslation(actor, "name") }}
        </h1>
        <Icon name="bi:person-vcard" class="display-5" />
      </div>
      <div class="card-body text-bg-dark">
        <div class="row justify-content-center align-items-center">
          <div class="col-12 col-lg-4 text-lg-end">
            <slot name="images"></slot>
          </div>
          <span class="col-12 col-lg-8">
            <span ref="shortBio" id="shortBio">
              <p v-for="p in getTranslation(actor, 'short_bio').split('\n')" class="lead">{{ p }}</p>
            </span>
            <button
              v-if="isTruncated"
              id="readMoreBtn"
              class="btn btn-light mt-3"
              data-bs-toggle="modal"
              data-bs-target="#fullTextModal"
            >
              {{ translations.more }}
            </button>
          </span>
        </div>
      </div>
      <div class="card-footer">
        <ActorQuote :quote="getTranslation(actor, 'quote')" />
      </div>
    </div>
    <ActorFullBioModal :close="getTranslation(translations, 'close')" />
  </div>
</template>

<style lang="css" scoped>
#idContainer {
  min-height: 45vw;
}

@media (max-width: 767px) {
  #shortBio {
    display: -webkit-box;
    -webkit-line-clamp: 10;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    word-wrap: break-word;
  }
}

@media (min-width: 768px) {
  #shortBio {
    display: -webkit-box;
    -webkit-line-clamp: 15;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    word-wrap: break-word;
  }
}

@media (min-width: 992px) {
  #shortBio {
    display: -webkit-box;
    -webkit-line-clamp: 9;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    word-wrap: break-word;
  }
}

@media (min-width: 1200px) {
  #shortBio {
    display: -webkit-box;
    -webkit-line-clamp: 14;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    word-wrap: break-word;
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
