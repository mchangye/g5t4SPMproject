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
                    <router-link to="/browseroles" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/browseroles' }">
                        <img src="../assets/browse.png" height="20" class="me-3">Browse Roles
                    </router-link>
                    <router-link to="/newrole" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/newrole' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Create New Role
                    </router-link>
                    <router-link to="/applicants" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/applicants' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Applicants
                    </router-link>
                    <router-link to="/" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test Landing
                    </router-link>
                    <router-link to="/about" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/about' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test About
                    </router-link>
                    <router-link to="/staffinfo" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/staffinfo' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test Staff Info
                    </router-link>
                    <router-link to="/rolesinfo" class="list-group-item list-group-item-action py-2 ripple" :class="{ 'active-link': $route.path === '/rolesinfo' }">
                        <i class="fas fa-chart-line fa-fw me-3"></i>Test Role Info
                    </router-link>
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

                

                <!-- Search form 
                <form class="d-none d-md-flex input-group w-auto my-auto">
                    <input autocomplete="off" type="search" class="form-control rounded"
                        placeholder='Search' style="min-width: 225px" />
                    <span class="input-group-text border-0"></span>
                </form>
                -->
                
                <!-- Right links -->
                <ul class="navbar-nav ms-auto d-flex flex-row">

                    <!-- Avatar -->
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle hidden-arrow d-flex align-items-center" href="#"
                            id="navbarDropdownMenuLink" role="button" data-mdb-toggle="dropdown" aria-expanded="false">
                            <img src="../assets/avatar-pic.jpg" class="rounded-circle"
                                height="50" alt="" loading="lazy" />
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownMenuLink">
                            <li><a class="dropdown-item" href="#">My profile</a></li>
                            <li><a class="dropdown-item" href="#">Settings</a></li>
                            <li><a class="dropdown-item" href="#">Logout</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
            
        </nav>
        
    </header>
    
</template>





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
  color: #007BFF; /* Change this to your preferred text color for active links */
  font-weight: bold; /* You can adjust the styling to your preference */
}


</style>