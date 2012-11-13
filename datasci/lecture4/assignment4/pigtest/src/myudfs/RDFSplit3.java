package myudfs;

import java.io.IOException;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.PatternSyntaxException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.lang.IllegalStateException;

import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;
import org.apache.pig.data.TupleFactory;

public class RDFSplit3 extends EvalFunc<Tuple> {
    private final static TupleFactory tupleFactory = TupleFactory.getInstance();
    private final static NQuadParser nquadParser = new NQuadParser();

    public Tuple exec(Tuple input) throws IOException {
        if (input == null || input.size() < 1)
            return null;
        try {
            String source = (String) input.get(0);
            if (source == null) {
                return null;
            }

            ArrayList<String> result = new ArrayList<String>(3);
            if ( nquadParser.parse(source,result) ) {
				return tupleFactory.newTupleNoCopy(result);
			} else {
            }
            return null;
        } catch (Exception e) {
			log.warn("offending string: "+input.get(0));
            log.error(e);
		}	
        // this only happens if the try block did not complete normally
        return null;
    }

	public static final class NQuadParser {
		int pos;
		String l; // current processing line
		
		private boolean skipWhiteSpace() {
			if ( pos < 0 ) return false;
			for ( ; pos < l.length(); ++pos ) {
				char ch = l.charAt(pos);
				if ( ch != ' ' && ch != '\t' ) break;
			}
			return pos < l.length();
		}
		
		private int skipNonWhiteSpace(int i) {
			char ch;
			for ( ; i < l.length(); ++i ) {
				ch = l.charAt(i);
				if ( ch == ' ' || ch == '\t' ) break;
			}
			return i;
		}
		
		private String extractSubject() {
			char ch = l.charAt(pos);
			int end = -1;
			if ( ch == '<' ) {
				// look for matching '>'
				end = l.indexOf('>',pos);
				if ( end >= 0 ) {
					++end;
				}
			} else if ( ch == '_') {
				// look for the first white space
				end = skipNonWhiteSpace(pos+1);
			} else {
				// screwed!
				pos = -1;
				return null;
			}
			int pos2 = pos;
			if ( end >= 0 ) {
				pos = end;
			} else {
				pos = -1;
			}
			return ( end < 0 ) ? null : l.substring(pos2, end);
		}
		
		private String extractPredicate() {
			if ( pos < 0 ) return null;
			
			char ch = l.charAt(pos);
			int end = -1;
			if ( ch == '<' ) {
				// look for matching '>'
				end = l.indexOf('>',pos);
				if ( end >= 0 ) {
					++end;
				}
			} else {
				// screwed!
				pos = -1;
				return null;
			}
			int pos2 = pos;
			if ( end >= 0 ) {
				pos = end;
			} else {
				pos = -1;
			}
			return ( end < 0 ) ? null : l.substring(pos2, end);
		}
		
		private String extractObject() {
			if ( pos < 0 ) return null;
			
			char ch = l.charAt(pos);
			int end = -1;
			if ( ch == '<' ) {
				// look for matching '>'
				end = l.indexOf('>',pos);
				if ( end >= 0 ) {
					++end;
				}
			} else if ( ch == '_') {
				// look for the first white space
				end = skipNonWhiteSpace(pos+1);
			} else if ( ch == '"' ) {
				// look for another quote
				int newEnd = end;
				while ( newEnd < l.length() ) {
					int xxx = l.indexOf('"',newEnd);
					// check whether it is escaped
					if ( xxx < 0 ) {
						pos = -1;
						return null;
					} else if ( l.charAt(xxx-1) != '\\' ) {
						// we got it right.
						end = xxx;
						break;
					}
					newEnd = xxx+1;
				}
				
				// sanity check
				if ( l.charAt(end) != '"' ) {
					pos = -1;
					return null;
				}
				
				// now skip all non-white spaces
				end = skipNonWhiteSpace(end);
			} else {
				// screwed!
				pos = -1;
				return null;
			}
			
			int pos2 = pos;
			if ( end >= 0 ) {
				pos = end;
			} else {
				pos = -1;
			}
			return ( end < 0 ) ? null : l.substring(pos2, end);	
		}
		
		public boolean parse(String s,List<String> res) {
            l = s;
			pos = 0;
            skipWhiteSpace(); // remove leading white space
            String subject = this.extractSubject();
			skipWhiteSpace();
            String predicate = this.extractPredicate();
			skipWhiteSpace();
            String object = this.extractObject();
			//skipWhiteSpace();
            //String context = this.extractObject();

            res.add(subject);
            res.add(predicate);
            res.add(object);
            //res.add(context);
			
			return subject != null && object != null && predicate != null;
		}
    }
}
