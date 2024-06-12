<script setup lang="ts">
const { data: translations } = useNuxtData("eventStrings");

const isCurrent = useState("isCurrent", () => ["true"]);
const selectedAudience = useState("selectedAudience", () => []);
const selectedGenres = useState("selectedGenres", () => []);

const hideFilters = (audienceType: string) => {
  if (audienceType === "adults") {
    return selectedAudience.value.length === 0 || selectedAudience.value.includes("adults");
  } else {
    return selectedAudience.value.length === 0 || selectedAudience.value.includes("children");
  }
};

const resetFilters = () => {
  isCurrent.value = ["true"];
  selectedAudience.value = [];
  selectedGenres.value = [];
};
</script>

<!-- TODO: Organize the template into smaller components.
E.g. input buttons should be converted to a component with props and imported.-->
<template lang="html">
  <div id="filterGroup" class="d-md-flex justify-content-between text-center mt-3">
    <div class="btn-group text-center" role="group" aria-label="Plays filter button group">
      <input
        v-model="isCurrent"
        type="checkbox"
        class="btn-check"
        id="currentFilter"
        value="true"
        autocomplete="on"
      />
      <label id="currentFilterLabel" class="btn btn-outline-primary me-2" for="currentFilter">
        {{ translations.current }}
      </label>

      <div class="dropdown">
        <button
          class="btn btn-primary dropdown-toggle me-2"
          type="button"
          data-bs-toggle="dropdown"
          data-bs-auto-close="outside"
          aria-expanded="false"
        >
          {{ translations.audience }}
        </button>
        <ul class="dropdown-menu">
          <li>
            <input
              v-model="selectedAudience"
              type="checkbox"
              class="btn-check"
              id="adultsFilter"
              value="adults"
              autocomplete="on"
            />
            <label class="btn btn-outline-primary filter-btn" for="adultsFilter">
              {{ translations.adults }}
            </label>
          </li>

          <li>
            <input
              v-model="selectedAudience"
              type="checkbox"
              class="btn-check"
              id="childrenFilter"
              value="children"
              autocomplete="on"
            />
            <label class="btn btn-outline-primary filter-btn" for="childrenFilter">
              {{ translations.children }}
            </label>
          </li>
        </ul>
      </div>

      <button
        id="genreFilterBtn"
        class="btn btn-primary dropdown-toggle"
        type="button"
        data-bs-toggle="dropdown"
        data-bs-auto-close="outside"
        aria-expanded="false"
      >
        {{ translations.genre }}
      </button>
      <ul class="dropdown-menu">
        <li v-if="hideFilters('adults')">
          <input
            v-model="selectedGenres"
            type="checkbox"
            class="btn-check"
            id="dramaFilter"
            value="drama"
            autocomplete="on"
          />
          <label class="btn btn-outline-primary filter-btn adults-filter" for="dramaFilter">
            {{ translations.drama }}
          </label>
        </li>

        <li v-if="hideFilters('adults')">
          <input
            v-model="selectedGenres"
            type="checkbox"
            class="btn-check"
            id="comedyFilter"
            value="comedy"
            autocomplete="on"
          />
          <label class="btn btn-outline-primary filter-btn adults-filter" for="comedyFilter">
            {{ translations.comedy }}
          </label>
        </li>

        <li v-if="hideFilters('adults')">
          <input
            v-model="selectedGenres"
            type="checkbox"
            class="btn-check"
            id="otherFilter"
            value="other"
            autocomplete="on"
          />
          <label class="btn btn-outline-primary filter-btn adults-filter" for="otherFilter">
            {{ translations.other }}
          </label>
        </li>

        <li v-if="hideFilters('children')">
          <input
            v-model="selectedGenres"
            type="checkbox"
            class="btn-check"
            id="puppetShowFilter"
            value="puppet-show"
            autocomplete="on"
          />
          <label class="btn btn-outline-primary filter-btn children-filter" for="puppetShowFilter">
            {{ translations.puppet }}
          </label>
        </li>

        <li v-if="hideFilters('children')">
          <input
            v-model="selectedGenres"
            type="checkbox"
            class="btn-check"
            id="childrenPlayFilter"
            value="children-play"
            autocomplete="on"
          />
          <label class="btn btn-outline-primary filter-btn children-filter" for="childrenPlayFilter">
            {{ translations.childPlay }}
          </label>
        </li>
      </ul>
    </div>
    <div class="btn-group d-block text-center mt-3 mt-md-0 me-0" role="group" aria-label="Reset button">
      <button @click="resetFilters" type="reset" class="btn btn-primary reset-btn">
        {{ translations.reset }}
      </button>
    </div>
  </div>
</template>

<style lang="css" scoped>
.filter-btn {
  width: 100%;
  border: 0px;
  text-align: start;
}
</style>

<style lang="css" scoped></style>
