<script setup lang="ts">
defineProps<{
  mainAccent?: {};
}>();

const { data: translations } = useNuxtData("homeStrings");
const displaySize = useState("displaySize");
</script>

<template lang="html">
  <div id="accentContainer" class="container mt-3 mb-3">
    <div class="row d-flex align-items-center">
      <div class="col-md-6 text-center">
        <!-- <img
          v-if="['xs', 'sm', 'md'].includes(displaySize)"
          :src="setThumborUrl(`/media/plays/${mainAccent.slug}/photos/7.jpg`, 'unsafe/315x0/filters:format(webp)')"
          id="mobileAccent"
          class="img-fluid img-thumbnail d-inline d-lg-none"
          alt=""
        />
        <img
          v-if="['lg', 'xl', 'xxl'].includes(displaySize)"
          :src="setThumborUrl(`/media/plays/${mainAccent.slug}/photos/7.jpg`, 'unsafe/610x0/filters:format(webp)')"
          id="desktopAccent"
          class="img-fluid img-thumbnail d-none d-lg-inline"
          alt=""
        /> -->
        <NuxtImg
          format="webp"
          :src="`/media/plays/${mainAccent.slug}/photos/7.jpg`"
          :alt="`Photo from: ${mainAccent.name}`"
          class="img-fluid img-thumbnail"
          sizes="100vw md:50vw"
        />
      </div>
      <div class="col-md-6 text-start mt-md-0">
        <h3 class="display-5 mt-2 mt-md-0">{{ getTranslation(mainAccent, "name") }}</h3>
        <hr />
        <span id="playDescription">
          <p v-for="p in getTranslation(mainAccent, 'short_description').split('\n')" class="lead">
            {{ p }}
          </p>
        </span>
        <div class="d-flex justify-content-between mt-3">
          <NuxtLinkLocale :to="`/events/plays/${mainAccent.slug}`" id="readMoreBtn" class="btn btn-primary">
            {{ translations.more }}
          </NuxtLinkLocale>
          <a
            tabindex="0"
            id="ticketButton"
            class="btn btn-primary"
            role="button"
            @click.prevent="openPopup(`https://www.entase.bg/book?eid=${mainAccent.entase_data[0].id}`)"
          >
            <i class="bi bi-ticket-perforated me-1"></i>
            {{ translations.ticket }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped>
#playDescription {
  display: -webkit-box;
  -webkit-line-clamp: 10;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}

p {
  display: inline;
}

p::after {
  content: "\A\A";
  white-space: pre;
}
</style>
