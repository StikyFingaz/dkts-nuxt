<script setup lang="ts">
const userLocale = useState("userLocale");

const { data: translations } = useNuxtData("eventStrings");
const { data: play } = useNuxtData("playData");

const ticketLink = play.value.entase_data?.[0]?.id ?? null;
const playDescription = ref(null);
const isTruncated = ref(false);

const scrollToTrailer = () => {
  const playTrailer = document.getElementById("trailerContainer");
  document.documentElement.style.scrollBehavior = "auto";
  window.scrollTo({
    top: playTrailer.offsetTop - 75,
  });

  setTimeout(() => {
    document.documentElement.style.scrollBehavior = "smooth";
  });
};

onMounted(() => {
  const descriptionElement = playDescription.value;
  const clientHeight = descriptionElement.clientHeight;
  const scrollHeight = descriptionElement.scrollHeight;

  isTruncated.value = clientHeight < scrollHeight;
});
</script>

<template lang="html">
  <div class="container mt-3">
    <div id="posterRow" class="row align-items-center">
      <div class="col-lg-6">
        <slot name="images"></slot>
      </div>
      <div class="col-lg-6">
        <h1 class="display-4 mt-3 mt-lg-0">{{ getTranslation(play, "name") }}</h1>
        <button
          v-if="play.has_trailer"
          class="btn btn-outline-primary border border-0 d-flex align-items-center"
          @click="scrollToTrailer"
        >
          <Icon name="bi:play-circle" class="me-2" />
          {{ translations.trailer }}
        </button>
        <hr />
        <slot name="description">
          <span ref="playDescription" id="playDescription">
            <p v-for="p in getTranslation(play, 'short_description').split('\n')" class="lead">{{ p }}</p>
          </span>
        </slot>
        <div class="d-flex justify-content-between mt-3 mb-3 mb-lg-0">
          <button
            v-if="isTruncated"
            id="readMoreBtn"
            class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#fullDescriptionModal"
          >
            {{ translations.more }}
          </button>
          <a
            v-if="ticketLink"
            tabindex="0"
            id="ticketButton"
            class="btn btn-primary d-flex align-items-center"
            role="button"
            :href="`https://www.entase.bg/book?eid=${ticketLink}&lc=${userLocale}`"
            @click.prevent="openTicketPopup(`https://www.entase.bg/book?eid=${ticketLink}&lc=${userLocale}`)"
          >
            <Icon name="bi:ticket-perforated" class="me-2" />
            {{ translations.ticket }}
          </a>
        </div>
      </div>
    </div>
    <PlayDescriptionModal
      :playName="getTranslation(play, 'name')"
      :fullDescription="getTranslation(play, 'short_description')"
      :close="translations.close"
    />
  </div>
</template>

<style lang="css" scoped>
#playDescription {
  display: -webkit-box;
  -webkit-line-clamp: 15;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}

p {
  display: inline;
}

p::after {
  content: " \A\A";
  white-space: pre;
}

@media (min-width: 1024px) {
  #posterRow {
    min-height: 87vh;
  }
}
</style>
