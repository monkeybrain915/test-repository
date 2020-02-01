void
 foo(const char *arbitrary_string, const char *and_another)
 {
 char onstack[8];#ifdef BAD
 /*
 * This first sprintf is bad behavior. Do not use sprintf!
 */
 sprintf(onstack, “%s, %s”, arbitrary_string, and_another);
 #else
 /*
 * The following two lines demonstrate better use of
 * snprintf().
 */
 snprintf(onstack, sizeof(onstack), “%s, %s”, arbitrary_string,
 and_another);
 #endif
 }
