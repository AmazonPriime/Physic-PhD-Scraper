<template>
    <div class="listing">
        <span class="title">
            {{ job.title }}
        </span>
        <span class="employer">
            Employer: <i>{{ job.employer }}</i>
        </span>
        <span class="description">
            {{ job.description }}
        </span>
        <span class="location">
            Location: <i>{{ job.location }}</i>
        </span>
        <span class="salary">
            Salary: <i>{{ job.salary }}</i>
        </span>
        <span class="date">
            Opened: <i>{{ job.date_placed }}</i>
        </span>
        <span class="date">
            Closes: <i>{{ job.date_closes }}</i>
        </span>
        <span>
            Website:
            <a :href="job.link" class="inner-link">
                <b>{{ job.link.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i)[1] }}</b>
            </a>
        </span>
        <a :href="job.link" target="_blank" class="button">
            Show Listing
        </a>
    </div>
</template>

<script>
export default {
  name: 'Listing',
  props: {
    job: {},
  },
};
</script>

<style scoped>
.listing {
    margin: 20px;
    margin-top: 0px;
    padding: 10px;
    background-color: rgba(189, 195, 199, 0.4);
    border-radius: 5px;
    backdrop-filter: blur(5px);
}

.listing span {
    display: block;
    margin-bottom: 10px;
    font-size: 14px;
}

.listing .title {
    font-weight: bold;
    margin-bottom: 0;
    font-size: 16px;
}

.listing .description {
    font-size: 16px;
}

.listing .salary,
.listing .date,
.listing .location {
    margin-bottom: 2px;
}

.listing .button {
    background-color: rgba(26, 188, 156, 1.0);
    text-decoration: none;
    color: white;
    display: block;
    text-align: center;
    margin: 10px;
    margin-bottom: 0;
    padding: 10px 0;
    border-radius: 10px;
    font-weight: bold;
}

.listing .inner-link {
    color: black;
}
</style>
