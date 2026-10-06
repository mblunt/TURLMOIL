-- uri_mime (Alire crate) URI parser
-- https://git.sr.ht/~nytpu/uri-mime-ada
--
-- RFC 3986 / RFC 3987 compliant parser. The URL record exposes each component
-- with an accompanying _Present boolean, so absent components are distinguished
-- from empty ones. Path is always present per RFC 3986 (may be empty string).

with Ada.Command_Line;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Text_IO;
with URI;

procedure Ada_Uri_Mime is

   function JSON_Escape (S : String) return String is
      R : Unbounded_String;
   begin
      for C of S loop
         case C is
            when '"'                => Append (R, "\""");
            when '\'                => Append (R, "\\");
            when Character'Val (8)  => Append (R, "\b");
            when Character'Val (9)  => Append (R, "\t");
            when Character'Val (10) => Append (R, "\n");
            when Character'Val (12) => Append (R, "\f");
            when Character'Val (13) => Append (R, "\r");
            when others             => Append (R, C);
         end case;
      end loop;
      return To_String (R);
   end JSON_Escape;

   function Nullable (S : String) return String is
   begin
      if S = "" then
         return "null";
      else
         return """" & JSON_Escape (S) & """";
      end if;
   end Nullable;

   function Nullable_If (Present : Boolean; S : Unbounded_String)
     return String is
   begin
      if not Present or else S = Null_Unbounded_String then
         return "null";
      else
         return """" & JSON_Escape (To_String (S)) & """";
      end if;
   end Nullable_If;

   function Try_Parse (Raw : String) return String is
      U    : constant URI.URL := URI.Parse (Raw);
      Port : constant String  :=
               (if U.Port_Present
                then URI.Port_Number'Image (U.Port) (2 .. URI.Port_Number'Image (U.Port)'Last)
                else "");
   begin
      return
        "{" &
        """scheme"":"    & Nullable_If (U.Scheme_Present,    U.Scheme)    & "," &
        """authority"":""EXCLUDE""," &
        """userinfo"":"  & Nullable_If (U.User_Info_Present, U.User_Info) & "," &
        """username"":""EXCLUDE""," &
        """password"":""EXCLUDE""," &
        """host"":"      & Nullable    (To_String (U.Host))               & "," &
        """port"":"      & Nullable    (Port)                             & "," &
        """path"":"      & Nullable    (To_String (U.Path))               & "," &
        """query"":"     & Nullable_If (U.Query_Present,    U.Query)      & "," &
        """query_dict"":""EXCLUDE""," &
        """fragment"":"  & Nullable_If (U.Fragment_Present, U.Fragment)   & "," &
        """raw_url"":"   & """" & JSON_Escape (Raw) & """" &
        "}";
   exception
      when URI.Invalid_Scheme =>
         return
           "{""error"":""Invalid URI scheme""," &
           """raw_url"":"   & """" & JSON_Escape (Raw) & """}";
      when others =>
         return
           "{""error"":""Failed to parse URI""," &
           """raw_url"":"   & """" & JSON_Escape (Raw) & """}";
   end Try_Parse;

begin
   if Ada.Command_Line.Argument_Count < 1 then
      Ada.Text_IO.Put_Line ("{""error"":""No URL provided""}");
      return;
   end if;
   Ada.Text_IO.Put_Line (Try_Parse (Ada.Command_Line.Argument (1)));
end Ada_Uri_Mime;
