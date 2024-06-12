<script setup lang="ts">
import Fuse from "fuse.js";

// Closing the menu can be done with a prop (parent -> child) as well.
// Below is demonstrated how emits (child -> parent) work.
const emit = defineEmits<{
  (e: "closeMenu"): void;
}>();

const props = defineProps<{
  placeholder?: str;
}>();

const searchData = useState("searchData");
const searchPattern = ref("");
const results = ref([]);

const performSearch = () => {
  const fuseOptions = {
    keys: ["name"],
    threshold: 0.5,
    distance: 20,
  };
  const fuse = new Fuse(searchData.value, fuseOptions);
  results.value = fuse.search(searchPattern.value);
};

const clearSearch = (result) => {
  searchPattern.value = "";
  results.value = [];
  emit("closeMenu");
};

const shortUrl = {
  actor: "/about/actors",
  play: "/events/plays",
};
</script>

<template lang="html">
  <div id="searchContainer">
    <form v-if="searchData" class="d-flex" role="search" @submit.prevent="performSearch">
      <input
        v-model="searchPattern"
        @input="performSearch"
        id="search"
        class="form-control"
        type="search"
        :placeholder="placeholder"
        aria-label="Search"
        autocomplete="off"
      />
    </form>
    <div class="d-flex mt-1 position-absolute search-results">
      <ul class="list-group">
        <NuxtLinkLocale
          v-for="result in results"
          :key="result.item.slug || result.item.nickname"
          :to="`${shortUrl[result.item.type]}/${result.item[result.item.param]}`"
          class="list-group-item list-group-item-action"
          @click="clearSearch"
        >
          {{ result.item.name }}
        </NuxtLinkLocale>
      </ul>
    </div>
  </div>
</template>

<style lang="css" scoped>
.search-results {
  z-index: 9999;
}
</style>
