<template>
  <div>
    <div class="filters">
      <div>
        <input
          type="text"
          class="filter-search"
          placeholder="Search filter"
          v-on:change="filter"
        >
      </div>
    </div>
    <div class="listings-container">
      <div v-if="!showFiltered">
        <div class="filter-details">
          Found <b>{{ jobs.length }}</b> positions!
        </div>
        <Listing v-for="job in jobs" :job="job" v-bind:key="job.link" class="not-filtered" />
        <div v-if="jobs.length === 0" class="no-listings">
          Hmm there seems to be no listings?
          <br />
          <img src="https://media4.giphy.com/media/Y15VREpz6N6MaPflI2/200w.gif?cid=82a1493b3ohkbl3ph8rqkcp09xzr3m51b05y8yjtpvk7mxwl&rid=200w.gif&ct=g">
        </div>
      </div>
      <div v-else>
        <div class="filter-details">
          <b>{{ filteredJobs.length }}</b> positions based on your filter!
        </div>
        <Listing v-for="job in filteredJobs" :job="job" v-bind:key="job.link" class="filtered" />
        <div v-if="filteredJobs.length === 0" class="no-listings">
          Hmm there seems to be no listings?
          <br />
          <img src="https://media4.giphy.com/media/Y15VREpz6N6MaPflI2/200w.gif?cid=82a1493b3ohkbl3ph8rqkcp09xzr3m51b05y8yjtpvk7mxwl&rid=200w.gif&ct=g">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Listing from './Listing.vue';

export default {
  name: 'ListingContainer',
  components: {
    Listing,
  },
  props: {
    jobs: [],
  },
  data() {
    return {
      filteredJobs: [],
      showFiltered: false,
    };
  },
  methods: {
    filter(event) {
      const query = event.target.value.toLowerCase();
      if (query.length === 0) {
        this.filteredJobs = [];
        this.showFiltered = false;
        return;
      }
      const queryWords = query.split(' ');
      const tempFilteredJobs = [];
      this.jobs.forEach((job) => {
        const title = job.title.toLowerCase();
        const desc = job.description.toLowerCase();
        const employer = job.employer.toLowerCase();
        const location = job.location.toLowerCase();
        queryWords.forEach((word) => {
          const inTitleDesc = title.includes(word) || desc.includes(word);
          const inEmployerLocation = employer.includes(word) || location.includes(word);
          if ((inTitleDesc || inEmployerLocation) && word !== '') {
            tempFilteredJobs.push(job);
          }
        });
      });
      this.filteredJobs = tempFilteredJobs;
      this.showFiltered = true;
    },
  },
};
</script>

<style scoped>
.search-details {
  text-align: center;
}
.listings-container {
  max-width: 1000px;
  margin: 0 auto;
}
.no-listings {
  margin: 20px;
  padding: 10px;
  background-color: rgba(189, 195, 199, 0.4);
  border-radius: 5px;
  backdrop-filter: blur(5px);
  text-align: center;
}
.no-listings img {
  margin-top: 10px;
}
.filters {
  gap: 1em;
  margin: 0 auto;
  margin-top: 10px;
  background-color: rgba(189, 195, 199, 0.4);
  backdrop-filter: blur(5px);
  max-width: 1000px;
  border-radius: 10px;
  padding: 10px;
  text-align: center;
}
.filter-search {
  padding: 5px;
  border-radius: 5px;
  border: 1px solid grey;
  max-width: 500px;
  width: 80%;
  font-size: 16px;;
  text-align: center;
}
.filter-details {
  margin: 10px;
  text-align: center;
}
</style>
