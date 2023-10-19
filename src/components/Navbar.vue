<template>
    <!--Main Navigation-->
    <header>
        <!-- Sidebar -->
        <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse bg-white mt-5">
            <!-- Brand -->
            <a class="navbar-brand ms-5 ps-3" href="/">
                <img src="../assets/sbrplogo.png" height="100" alt="" loading="lazy" />
            </a>
            <div class="position-sticky">
                <div class="list-group list-group-flush mx-3 mt-4">
                    <!-- This Browseroles is for Staff -->
                    <router-link to="/browserolesstaff" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/browserolesstaff' }" v-if="isStaff">
                        <img src="../assets/browse.png" height="20" class="me-3">Browse Roles (Staff)
                    </router-link>
                    <!-- This Browseroles is for HR -->
                    <router-link to="/browseroleshr" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/browseroleshr' }" v-if="isManagement">
                        <img src="../assets/browse.png" height="20" class="me-3">Browse Roles (HR)
                    </router-link>
                    <router-link to="/newrole" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/newrole' }" v-if="isManagement">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Create New Role
                    </router-link>
                    <router-link to="/myapplications" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/myapplications' }" v-if="isStaff">
                        <i class="fas fa-chart-line fa-fw me-3"></i>My Applications
                    </router-link>
                    <router-link to="/" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test Landing
                    </router-link>
                    <!-- <router-link to="/about" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/about' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test About
                    </router-link> -->
                    <router-link to="/staffinfo" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/staffinfo' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test Staff Info
                    </router-link>
                    <router-link to="/rolesinfo" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/rolesinfo' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test Role Info
                    </router-link>
                    <router-link to="/updateskill" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/updateskill' }" v-if="isManagement">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Update Skill (Staff)
                    </router-link>
                    <router-link to="/applyrole" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/applyrole' }" v-if="isManagement">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Apply Role (Staff)
                    </router-link>
                    <RouterLink :to="'/profile/' + this.staffId"><button class="btn btn-primary">Profile</button></RouterLink>
                    <button class="btn btn-primary">Notifications</button>
                </div>
            </div>
        </nav>


        <!-- Navbar -->
        <nav id="main-navbar" class="navbar navbar-expand-lg navbar-light bg-white fixed-top">
            <!-- Container wrapper -->
            <div class="container-fluid">
                <!-- Toggle button -->
                <button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#sidebarMenu"
                    aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
                    <i class="fas fa-bars"></i>
                </button>


                <span>Welcome, {{ this.userFirstName }} {{ this.userLastName }}</span>

                <!-- Search form 
                <form class="d-none d-md-flex input-group w-auto my-auto">
                    <input autocomplete="off" type="search" class="form-control rounded"
                        placeholder='Search' style="min-width: 225px" />
                    <span class="input-group-text border-0"></span>
                </form>
                -->

                <!-- Right links -->
                <ul class="navbar-nav ms-auto d-flex flex-row">
                    
                    <!-- Notification dropdown -->
                    <li class="nav-item dropdown">
                        <a class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow" href="#" id="navbarDropdownMenuLink"
                            role="button" data-mdb-toggle="dropdown" aria-expanded="false">
                            <i class="fas fa-bell"></i>
                            <span class="badge rounded-pill badge-notification bg-danger">1</span>
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownMenuLink">
                            <li><a class="dropdown-item" href="#">Some news</a></li>
                            <li><a class="dropdown-item" href="#">Another news</a></li>
                            <li>
                                <a class="dropdown-item" href="#">Something else here</a>
                            </li>
                        </ul>
                    </li>

                    <!-- Avatar -->
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle hidden-arrow d-flex align-items-center" href="#"
                            id="navbarDropdownMenuLink" role="button" data-mdb-toggle="dropdown" aria-expanded="false">
                            <img src="../assets/avatar-pic.jpg" class="rounded-circle" height="50" alt="" loading="lazy" />
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownMenuLink">
                            <li><a class="dropdown-item" :href="'/profile/' + this.staffId">My profile</a></li>
                            <li><a class="dropdown-item" href="#">Settings</a></li>
                            <li><a class="dropdown-item" href="/" @click="resetStaffId">Logout</a></li>
                        </ul>
                    </li>
                </ul>
            </div>

        </nav>

    </header>
</template>


<script>
import eventBus from '@/event-bus';

export default {
    data() {
        return {
            userAccessLevel: '',
            isManagement: false,
            isStaff: false,
            userFirstName: '',
            userLastName: '',
        };
    },
    created() {
        // Access the staff_id from the event bus
        this.staffId = eventBus.getStaffId();
        this.getAccessLevel();
    },
    methods: {
        resetStaffId() {
            // Clear the staff_id in localStorage
            localStorage.removeItem('staff_id');

            // Also clear it from your component's data
            this.staffId = null;

        },
        getAccessLevel() {
            fetch(`http://localhost:5000/api/get-staff-info/` + this.staffId)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Network response failed');
                    }
                    return response.json();
                })
                .then((data) => {
                    this.userFirstName = data.Staff_FName;
                    this.userLastName = data.Staff_LName;
                    this.userAccessLevel = data.Access_ID;
                    this.isManagement = ["Manager", "HR", "Admin"].includes(data.Access_ID);
                    this.isStaff = ["User"].includes(data.Access_ID);
                })
                .catch((error) => {
                    console.error('There was a problem with the getStaffInfoAPI fetch operation:', error);
                });
        },
    },


};

</script>



<style scoped>
body {
    background-color: #fbfbfb;
}

@media (min-width: 991.98px) {
    main {
        padding-left: 240px;
    }
}

/* Sidebar */
.sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    padding: 58px 0 0;
    /* Height of navbar */
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
    width: 240px;
    z-index: 600;
}

@media (max-width: 991.98px) {
    .sidebar {
        width: 100%;
    }
}

.sidebar .active {
    border-radius: 5px;
    box-shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);
}

.sidebar-sticky {
    position: relative;
    top: 0;
    height: calc(100vh - 48px);
    padding-top: 0.5rem;
    overflow-x: hidden;
    overflow-y: auto;
    /* Scrollable contents if viewport is shorter than content. */
}

.active-link {
    color: #007BFF;
    /* Change this to your preferred text color for active links */
    font-weight: bold;
    /* You can adjust the styling to your preference */
}</style>