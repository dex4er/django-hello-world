This example requires additional patch for Django:

```patch
diff --git a/django/contrib/admin/templatetags/admin_list.py b/django/contrib/admin/templatetags/admin_list.py
index f4033e2..9e70f8c 100644
--- a/django/contrib/admin/templatetags/admin_list.py
+++ b/django/contrib/admin/templatetags/admin_list.py
@@ -199,7 +199,10 @@ def items_for_result(cl, result, form):
         empty_value_display = cl.model_admin.get_empty_value_display()
         row_classes = ['field-%s' % field_name]
         try:
-            f, attr, value = lookup_field(field_name, result, cl.model_admin)
+            if isinstance(result, dict):
+                f, attr, value = None, field_name, result.get(field_name)
+            else:
+                f, attr, value = lookup_field(field_name, result, cl.model_admin)
         except ObjectDoesNotExist:
             result_repr = empty_value_display
         else:
```
