/* Account entry is visible from Home without changing the guest review. */
const accountHome147=home;
home=()=>accountHome147().replace('</header>','</header><div class="account-home-entry147"><button type="button" class="btn secondary" data-action="account">'+(state.account?Arabic169.primary("حسابي","ui"):Arabic169.primary("دخول / حساب","ui"))+'</button></div>');
